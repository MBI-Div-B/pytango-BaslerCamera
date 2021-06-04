# pytango-BaslerCamera
This tango device connects to Basler cameras by writing the serial number of it (serial_number as a device property) and returns the image of the camera. Written in python3.
In order to be used one needs to install first pypylon (pip install pypylon). Maybe pylon needs to be installed as well (before installing pypylon) if this has not been done yet.

The attributes of this class are:
- image
- friendly_name
- real_serial_number
- model_name
- exposure (W)
- exposure_min
- exposure_max
- gain (W)
- gain_min
- gain_max
- width (W)
- width_min
- width_max
- height (W)
- height_min
- height_max
- offsetX (W)
- offsetY (W)
- format_pixel (W)
- report_framerate
- binning_horizontal (W)
- binning_vertical (W)
- sensor_readout_mode
The attributes with a (W) next to the name are WRITE att. as well.
