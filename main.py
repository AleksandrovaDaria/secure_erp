from model import HRModel
from view import HRView
from controller import HRController

if __name__ == '__main__':
    model = HRModel()
    view = HRView()
    controller = HRController(model, view)
    controller.run()
