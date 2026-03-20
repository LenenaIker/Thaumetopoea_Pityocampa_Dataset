import omni.replicator.core as rep


def run_orchestrator(app):
    rep.orchestrator.run()

    while not rep.orchestrator.get_is_started():
        app.update()

    while rep.orchestrator.get_is_started():
        app.update()

    rep.BackendDispatch.wait_until_done()
    rep.orchestrator.stop()
