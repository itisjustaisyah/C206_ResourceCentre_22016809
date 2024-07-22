from inventory.inventory import Inventory


class Test_US_04:
    test_inventory = Inventory()
    test_inventory.addAsset("Camera", "C001", "Test camera 1", 5)
    test_inventory.addAsset("Camera", "C002", "Test camera 2", 10)
    test_inventory.addAsset("Camera", "C003", "Test camera 3", 15)

    test_inventory.addAsset("Laptop", "L001", "Test Laptop 1", "WINXP")
    test_inventory.addAsset("Laptop", "L002", "Test Laptop 2", "MACOS")
    test_inventory.addAsset("Laptop", "L003", "Test Laptop 3", "WINXP")

    def test_getAvailableCamera_AllAvailable(self):
        ti1 = self.test_inventory
        result = ti1.getAvailableAsset("Camera")
        assert result == [ti1.cameraList[0], ti1.cameraList[1], ti1.cameraList[2]]

    def test_getAvailableCamera_1UnAvailable(self):
        ti2 = self.test_inventory
        ti2.cameraList[1].setIsAvailable(False)
        result = ti2.getAvailableAsset("Camera")
        assert result == [ti2.cameraList[0], ti2.cameraList[2]]

    def test_getAvailableCamera_2UnAvailable(self):
        ti3 = self.test_inventory
        ti3.cameraList[1].setIsAvailable(True)
        ti3.cameraList[0].setIsAvailable(False)
        ti3.cameraList[2].setIsAvailable(False)
        result = ti3.getAvailableAsset("Camera")
        assert result == [ti3.cameraList[1]]

    def test_getAvailableCamera_AllUnAvailable(self):
        ti4 = self.test_inventory
        ti4.cameraList[0].setIsAvailable(False)
        ti4.cameraList[1].setIsAvailable(False)
        ti4.cameraList[2].setIsAvailable(False)
        result = ti4.getAvailableAsset("Camera")
        assert result == []

    def test_getAvailableLaptop_AllAvailable(self):
        ti5 = self.test_inventory
        result = ti5.getAvailableAsset("Laptop")
        assert result == [ti5.laptopList[0], ti5.laptopList[1], ti5.laptopList[2]]

    def test_getAvailableLaptop_1UnAvailable(self):
        ti6 = self.test_inventory
        ti6.laptopList[1].setIsAvailable(False)
        result = ti6.getAvailableAsset("Laptop")
        assert result == [ti6.laptopList[0], ti6.laptopList[2]]

    def test_getAvailableLaptop_2UnAvailable(self):
        ti7 = self.test_inventory
        ti7.laptopList[1].setIsAvailable(True)
        ti7.laptopList[0].setIsAvailable(False)
        ti7.laptopList[2].setIsAvailable(False)
        result = ti7.getAvailableAsset("Laptop")
        assert result == [ti7.laptopList[1]]

    def test_getAvailableLaptop_AllUnAvailable(self):
        ti8 = self.test_inventory
        ti8.laptopList[0].setIsAvailable(False)
        ti8.laptopList[1].setIsAvailable(False)
        ti8.laptopList[2].setIsAvailable(False)
        result = ti8.getAvailableAsset("Laptop")
        assert result == []
        