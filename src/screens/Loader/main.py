from src.screens.Loader.frontend import frontend
from src.screens.Loader.backend import backend

class LoaderScreen:
    def __init__(self, window):
        frontend.Frontend(window)
        backend.Backend(window.root)
    