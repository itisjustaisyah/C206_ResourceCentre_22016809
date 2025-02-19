from inventory.camera import Camera
from inventory.laptop import Laptop


class Inventory:
    def __init__(self):
        self.cameraList = []
        self.laptopList = []

        # Prepare the data (Inventory list)

    # def addAsset(self, assetTag, description, os):
    #     # Check for correct values
    #     correct = True
    #     if len(assetTag) == 0 or len(description) == 0 or len(os) == 0:
    #         correct = False
    #         error_message = "Incorrect values."
    #     # Refactor (C): Extract long methods to findLaptop(assetTag),
    #     # return the found laptop, return None if not found.
    #     # **Don't forget to create test cases for this new method.
    #     # Check for existing laptop
    #     notExist = True
    #     for l in self.laptopList:
    #         currentTag = l.getAssetTag()
    #         if currentTag == assetTag:
    #             notExist = False
    #             error_message = "Asset already exists."
    #     if correct and notExist:
    #         new_laptop = Laptop(assetTag, description, os)
    #         self.laptopList.append(new_laptop)
    #         return True
    #     else:
    #         print(error_message)
    #         return False
    # #
    # def addAsset(self, assetTag, description, opticalzoom):
    #     # Check for correct values
    #     correct = True
    #     if len(assetTag) == 0 or len(description) == 0 or opticalzoom < 0:
    #         correct = False
    #     error_message = "Incorrect values."
    #     # Refactor (C): Extract long methods to findCamera(assetTag),
    #     # return the found camera, return None if not found.
    #     # **Don't forget to create test cases for this new method.
    #     # Check for existing camera
    #     notExist = True
    #     for c in self.cameraList:
    #         currentTag = c.getAssetTag()
    #         if currentTag == assetTag:
    #             notExist = False
    #             error_message = "Asset already exists."
    #     if correct and notExist:
    #         new_camera = Camera(assetTag, description, opticalzoom)
    #         self.cameraList.append(new_camera)
    #         return True
    #     else:
    #         print(error_message)
    #         return False
    def addAsset(self, assetType, assetTag, description, attribute):
        error_message = ""
        correct = True
        if len(assetTag) == 0 or len(description) == 0 or (type(attribute) == int and attribute < 0) or (type(attribute) == str and len(attribute) == 0):
            correct = False
            error_message = "Incorrect values."
        # Refactor (C): Extract long methods to findLaptop(assetTag),
        # return the found asset, return None if not found.
        # Check for existing asset
        notExist = True
        if self.findAsset(assetTag) is not None:
            notExist = False
            error_message = "Asset already exists."
        if correct and notExist:
            if assetType == "Camera":
                new_asset = Camera(assetTag, description, attribute)
                self.cameraList.append(new_asset)
                return True
            elif assetType == "Laptop":
                new_asset = Laptop(assetTag, description, attribute)
                self.laptopList.append(new_asset)
                return True
        else:
            print(error_message)
            return False

    def getAvailableAsset(self, assetType):
        if assetType == "Camera":
            available_camera = []
            for c in self.cameraList:
                if c.getIsAvailable() == "Yes":
                    available_camera.append(c)
            return available_camera
        elif assetType == "Laptop":
            available_laptop = []
            for l in self.laptopList:
                if l.getIsAvailable() == "Yes":
                    available_laptop.append(l)
            return available_laptop

    def loanAsset(self, assetTag, dueDate):
        success = False
        if len(assetTag) > 0 and len(dueDate) > 0:
            # Refactor (C): use findCamera()
            i = self.findAsset(assetTag)
            if i is not None and i.getIsAvailable() == "Yes":
                i.setIsAvailable(False)
                i.setDueDate(dueDate)
                success = True
        return success

    # def loanAsset(self, assetTag, dueDate):
    #     success = False
    #     if len(assetTag) > 0 and len(dueDate) > 0:
    #         # Refactor (C): use findCamera()
    #         for i in self.cameraList:
    #             if i.getAssetTag() == assetTag:
    #                 if i.getIsAvailable() == "Yes":
    #                     i.setIsAvailable(False)
    #                     i.setDueDate(dueDate)
    #                     success = True
    #
    #     return success
    #
    # def loanAsset(self, assetTag, dueDate):
    #     success = False
    #     if len(assetTag) > 0 and len(dueDate) > 0:
    #         # Refactor (C): use findcamera()
    #         for i in self.laptopList:
    #             if i.getAssetTag() == assetTag:
    #                 if i.getIsAvailable() == "Yes":
    #                     i.setIsAvailable(False)
    #                     i.setDueDate(dueDate)
    #                     success = True
    #
    #     return success

    # def returnAsset(self, assetTag):
    #     success = False
    #     if len(assetTag) > 0:
    #         # Refactor (C): use findcamera()
    #         for i in self.cameraList:
    #             if i.getAssetTag() == assetTag:
    #                 if i.getIsAvailable() == "No":
    #                     i.setIsAvailable(True)
    #                     i.setDueDate("")
    #                     success = True
    #
    #     return success
    #
    # def returnAsset(self, assetTag):
    #     success = False
    #     if len(assetTag) > 0:
    #         # Refactor (C): use findcamera()
    #         for i in self.laptopList:
    #             if i.getAssetTag() == assetTag:
    #                 if i.getIsAvailable() == "No":
    #                     i.setIsAvailable(True)
    #                     i.setDueDate("")
    #                     success = True
    #
    #     return success

    def returnAsset(self, assetTag):
        asset = self.findAsset(assetTag)
        if asset is not None:
            if asset.getIsAvailable() == "No":
                asset.setIsAvailable(True)
                asset.setDueDate("")
                return True
        return False

    def findAsset(self, assetTag):
        for i in self.cameraList:
            if i.getAssetTag() == assetTag:
                return i
        for i in self.laptopList:
            if i.getAssetTag() == assetTag:
                return i
        return None

    def getNotAvailableCamera(self):
        table = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", "Description", "Available", "Due Date", "Zoom")
        if len(self.cameraList) <= 0:
            table += "There is no camera to display."
        for camera in self.cameraList:
            if camera.getIsAvailable() == "No":
                table += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(camera.getAssetTag(), camera.getDescription(),
                                                                   camera.getIsAvailable(), camera.getDueDate(),
                                                                   camera.getOpticalZoom())
        return table

    def getNotAvailableLaptop(self):
        table = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", "Description", "Available", "Due Date", "OS")
        if len(self.laptopList) <= 0:
            table += "There is no laptop to display."
        for laptop in self.laptopList:
            if laptop.getIsAvailable() == "No":
                table += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(laptop.getAssetTag(), laptop.getDescription(),
                                                                   laptop.getIsAvailable(), laptop.getDueDate(),
                                                                   laptop.getOS())

        return table
