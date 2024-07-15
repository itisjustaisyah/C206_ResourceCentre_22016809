from inventory.camera import Camera
from inventory.laptop import Laptop


class Inventory():
    def __init__(self):
        self.cameraList = []
        self.laptopList = []

        ## Prepare the data (Inventory list)

    def addLaptop(self, assetTag, description, os):
        # Check for correct values
        correct = True
        if len(assetTag) == 0 or len(description) == 0 or len(os) == 0:
            correct = False
            error_message = "Incorrect values."
        # Refactor (C): Extract long methods to findLaptop(assetTag),
        # return the found laptop, return None if not found.
        # **Don't forget to create test cases for this new method.
        # Check for existing laptop
        notExist = True
        for l in self.laptopList:
            currentTag = l.getAssetTag()
            if currentTag == assetTag:
                notExist = False
                error_message = "Asset already exists."
        if correct and notExist:
            new_laptop = Laptop(assetTag, description, os)
            self.laptopList.append(new_laptop)
            return True
        else:
            print(error_message)
            return False

    def addCamera(self, assetTag, description, opticalzoom):
        # Check for correct values
        correct = True
        if len(assetTag) == 0 or len(description) == 0 or opticalzoom < 0:
            correct = False
        error_message = "Incorrect values."
        # Refactor (C): Extract long methods to findCamera(assetTag),
        # return the found camera, return None if not found.
        # **Don't forget to create test cases for this new method.
        # Check for existing camera
        notExist = True
        for c in self.cameraList:
            currentTag = c.getAssetTag()
            if currentTag == assetTag:
                notExist = False
                error_message = "Asset already exists."
        if correct and notExist:
            new_camera = Camera(assetTag, description, opticalzoom)
            self.cameraList.append(new_camera)
            return True
        else:
            print(error_message)
            return False

    def getAvailableCamera(self):
        available_camera = []
        for c in self.cameraList:
            if c.getIsAvailable() == "Yes":
                available_camera.append(c)
        return available_camera

    def getAvailableLaptop(self):
        available_laptop = []
        for l in self.laptopList:
            if l.getIsAvailable() == "Yes":
                available_laptop.append(l)
        return available_laptop

    def loanCamera(self, assetTag, dueDate):
        success = False
        if len(assetTag) > 0 and len(dueDate) > 0:
            # Refactor (C): use findCamera()
            for i in self.cameraList:
                if i.getAssetTag() == assetTag:
                    if i.getIsAvailable() == "Yes":
                        i.setIsAvailable(False)
                        i.setDueDate(dueDate)
                        success = True

        return success

    def loanLaptop(self, assetTag, dueDate):
        success = False
        if len(assetTag) > 0 and len(dueDate) > 0:
            # Refactor (C): use findcamera()
            for i in self.laptopList:
                if i.getAssetTag() == assetTag:
                    if i.getIsAvailable() == "Yes":
                        i.setIsAvailable(False)
                        i.setDueDate(dueDate)
                        success = True

        return success

    def returnCamera(self, assetTag):
        success = False
        if len(assetTag) > 0:
            # Refactor (C): use findcamera()
            for i in self.cameraList:
                if i.getAssetTag() == assetTag:
                    if i.getIsAvailable() == "No":
                        i.setIsAvailable(True)
                        i.setDueDate("")
                        success = True

        return success

    def returnLaptop(self, assetTag):
        success = False
        if len(assetTag) > 0:
            # Refactor (C): use findcamera()
            for i in self.laptopList:
                if i.getAssetTag() == assetTag:
                    if i.getIsAvailable() == "No":
                        i.setIsAvailable(True)
                        i.setDueDate("")
                        success = True

        return success
