from pxr import Usd, UsdGeom, Gf # pyright: ignore[reportMissingImports]


class UsdMetricResolver:
    def __init__(self, target_stage):
        self.target_mpu = float(UsdGeom.GetStageMetersPerUnit(target_stage))
        if self.target_mpu <= 0.0:
            raise ValueError(f"Invalid target stage metersPerUnit: {self.target_mpu}")

        self._cache: dict[str, tuple[float, float, float]] = {}
        # asset_path -> (asset_mpu, unit_correction_scale, canonical_world_height)

    def resolve(self, asset_path: str) -> tuple[float, float, float]:
        cached = self._cache.get(asset_path)
        if cached is not None:
            return cached

        stage = Usd.Stage.Open(asset_path)
        if stage is None:
            raise RuntimeError(f"Could not open USD asset: {asset_path}")

        asset_mpu = float(UsdGeom.GetStageMetersPerUnit(stage))
        if asset_mpu <= 0.0:
            raise ValueError(f"Invalid asset metersPerUnit for {asset_path}: {asset_mpu}")

        unit_correction_scale = asset_mpu / self.target_mpu
        canonical_asset_height = self._measure_asset_height(stage)
        canonical_world_height = canonical_asset_height * unit_correction_scale

        result = (asset_mpu, unit_correction_scale, canonical_world_height)
        self._cache[asset_path] = result
        return result

    def _measure_asset_height(self, stage) -> float:
        root = stage.GetDefaultPrim()
        if not root or not root.IsValid():
            raise RuntimeError(f"No valid default prim in {stage.GetRootLayer().realPath}")

        bbox_cache = UsdGeom.BBoxCache(
            Usd.TimeCode.Default(),
            includedPurposes=[
                UsdGeom.Tokens.default_,
                UsdGeom.Tokens.render,
                UsdGeom.Tokens.proxy,
            ],
            useExtentsHint=True,
            ignoreVisibility=False,
        )

        # Primer intento: medir el default prim completo
        height = self._height_from_bound(bbox_cache.ComputeWorldBound(root))
        if height > 0.0:
            return height

        # Fallback: recorrer descendientes y quedarse con el mayor bbox válido
        best_height = 0.0
        best_path = None

        for prim in Usd.PrimRange(root):
            if not prim.IsValid():
                continue

            imageable = UsdGeom.Imageable(prim)
            if not imageable:
                continue

            bound = bbox_cache.ComputeWorldBound(prim)
            h = self._height_from_bound(bound)

            if h > best_height:
                best_height = h
                best_path = prim.GetPath()

        if best_height > 0.0:
            print(f"[USD METRICS] Fallback bbox for {stage.GetRootLayer().realPath} from prim {best_path} -> height={best_height:.4f}")
            return best_height

        raise ValueError(
            f"Could not compute positive height for asset: {stage.GetRootLayer().realPath}"
        )

    @staticmethod
    def _height_from_bound(bound) -> float:
        box = bound.GetBox()
        min_pt = box.GetMin()
        max_pt = box.GetMax()

        if min_pt == max_pt:
            return 0.0

        height = float(max_pt[2] - min_pt[2])
        if height <= 0.0 or abs(height) > 1e4 :
            return 0.0

        return height