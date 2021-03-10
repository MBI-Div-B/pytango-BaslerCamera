#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import tango
from tango import AttrWriteType, DevState, DispLevel, DevFloat
from tango.server import Device, attribute, command, device_property
from pypylon import pylon


class Basler(Device):
    '''
    Basler
    This controls the connection to Basler Cameras
    '''
 
    image = attribute(name='image', label='Basler image', max_dim_x=4096,
                      max_dim_y=4096, dtype=((DevFloat,),), access=AttrWriteType.READ)
    
    no_images = attribute(name='no_images', label='Number of images to grab', 
                          dtype="int", access=AttrWriteType.READ_WRITE)
    
    #S/N written on th e camera
    serial_number = device_property(dtype="str")
    
    __no_of_images = 1

    def init_device(self):
        # connect to camera
        Device.init_device(self)
        self.set_state(DevState.INIT)

        try:
            self.device = self.get_camera_device()
    
            # VERY IMPORTANT STEP! To use Basler PyPylon OpenCV viewer you have to call .Open() method on you camera
            if self.device is not None:
                instance = pylon.TlFactory.GetInstance()
                
                self.camera = pylon.InstantCamera(instance.CreateDevice(self.device))
                self.camera.Open()
            
            self.debug_stream('Init was done to camera with serial: {:s}'.format(self.device.GetSerialNumber()))
            self.set_state(DevState.ON)
        except:
            self.error_stream('Could not open camera')
            self.set_state(DevState.OFF)
 
         

    def get_camera_device(self):
        self.debug_stream('get_camera_device')
        for device in pylon.TlFactory.GetInstance().EnumerateDevices():
            if device.GetSerialNumber() == self.serial_number:
                return device
        
        return None
        
    def read_image(self):
        # Print the model name of the camera.
        self.debug_stream("Using device ")#, self.camera.GetDeviceInfo().GetModelName())
        self.camera.ExposureTimeRaw.SetValue(500)
        self.camera.StartGrabbingMax(self.__no_of_images)

        while self.camera.IsGrabbing():
            self.grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        
            if self.grabResult.GrabSucceeded():
                self.img = self.grabResult.Array
        
            self.grabResult.Release()
                
        return self.img
        
    def read_no_images(self):
        return self.__no_of_images
        
        
    def write_no_images(self, value):
        self.__no_of_images = value
        
    def delete_device(self):
        try:
            self.debug_stream('Close connection to camera with serial: {:s}'.format(self.device.GetSerialNumber()))
            self.camera.Close()
        except:
            return
             
    
    
if __name__ == "__main__":
    Basler.run_server()
    
    
    
    

