# class animal:
#     def reproduce(self):
#         pass

# class whale (animal):
#     def reproduce(self):
#         print('The whale was created ...')


# class mosquito (animal):
#     def reproduceMosquito(self):
#         print('This is a Mosquito object created today...')

# whale1=whale()
# whale1.reproduce()
# animal1=animal()
# animal1.reproduce()
# mos=mosquito()
# mos.reproduceMosquito



# from abc import ABC, abstractmethod

# class animal(ABC):
#     @abstractmethod
#     def reproduce(self):
#         pass

# class whale(animal):
#     pass

# animal1=animal()
# animal1.reproduce()

# whale1=whale()
# whale1.reproduce()


from abc import ABC , abstractmethod
class appleDeviceInterface(ABC):
    @abstractmethod
    def generatedID(self):
        return 'Defult implementtion of device ID: 0'

    @abstractmethod
    def returnSignalFromMainBus(self):
        pass

    @abstractmethod
    def connectWithAICloud(self):
        pass

class metaversGlasses(appleDeviceInterface):
    def generatedID(self):
        return 'ID544145487'
    
    def returnSignalFromMainBus(self):
        return '0x8451c3553c3c'
    
glasses = metaversGlasses()
print(glasses.generatedID())
print(glasses.returnSignalFromMainBus())

class MRGlasses(appleDeviceInterface):
    def generatedID(self):
        return super().generatedID()
    
    def returnSignalFromMainBus(self):
        return super().returnSignalFromMainBus()
    
    def connectWithAICloud(self):
        return super().connectWithAICloud()
    
mr=MRGlasses()
print(mr.generatedID())
print(mr.returnSignalFromMainBus())