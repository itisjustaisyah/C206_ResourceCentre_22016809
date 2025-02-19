from inventory.inventory import Inventory


class Test_US_07:
    ############### Test return camera ######################
    def test_return_camera_onLoan(self):
        test_inventory = Inventory()
        test_inventory.addAsset("Camera", "C001", "Test camera 1", 5)
        tested_camera = test_inventory.cameraList[0]
        result = test_inventory.loanAsset(tested_camera.getAssetTag(), "08-08-2030")
        assert result == True
        assert tested_camera.getDueDate() == "08-08-2030"
        assert tested_camera.getIsAvailable() == "No"

        result2 = test_inventory.returnAsset(tested_camera.getAssetTag())

        assert result2 == True
        assert tested_camera.getDueDate() == ""
        assert tested_camera.getIsAvailable() == "Yes"

    def test_return_camera_not_onLoan(self):
        test_inventory = Inventory()
        test_inventory.addAsset("Camera", "C001", "Test camera 1", 5)
        tested_camera = test_inventory.cameraList[0]

        result = test_inventory.returnAsset(tested_camera.getAssetTag())

        assert result == False
        assert tested_camera.getDueDate() == ""
        assert tested_camera.getIsAvailable() == "Yes"

    def test_return_camera_not_exists(self):
        test_inventory = Inventory()
        result = test_inventory.addAsset("Camera", "C001", "Test camera 1", 5)

        result = test_inventory.returnAsset("C003")

        assert result == False

    ############### Test return laptop ######################
    def test_return_laptop_onLoan(self):
        test_inventory = Inventory()
        test_inventory.addAsset("Laptop", "L001", "Test Laptop 1", "WINXP")
        tested_laptop = test_inventory.laptopList[0]
        result = test_inventory.loanAsset(tested_laptop.getAssetTag(), "08-08-2030")
        assert result == True
        assert tested_laptop.getDueDate() == "08-08-2030"
        assert tested_laptop.getIsAvailable() == "No"

        result2 = test_inventory.returnAsset(tested_laptop.getAssetTag())
        assert result2 == True
        assert tested_laptop.getDueDate() == ""
        assert tested_laptop.getIsAvailable() == "Yes"

    def test_return_laptop_not_onLoan(self):
        test_inventory = Inventory()
        test_inventory.addAsset("Laptop", "L001", "Test Laptop 1", "WINXP")
        tested_laptop = test_inventory.laptopList[0]

        result = test_inventory.returnAsset(tested_laptop.getAssetTag())

        assert result == False
        assert tested_laptop.getDueDate() == ""
        assert tested_laptop.getIsAvailable() == "Yes"

    def test_return_laptop_not_exists(self):
        test_inventory = Inventory()
        test_inventory.addAsset("Laptop", "L001", "Test Laptop 1", "WINXP")

        result = test_inventory.returnAsset("L003")

        assert result == False
