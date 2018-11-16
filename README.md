# heart_rate_sentinel_server

[![Build Status](https://travis-ci.com/HanxinHua/heart_rate_sentinel_server.svg?branch=master)](https://travis-ci.com/HanxinHua/heart_rate_sentinel_server)

This server will be built to receive POST requests from mock patient heart rate monitors that contain patient heart rate information over time. If a patient exhibits a tachycardic heart rate, the physician should receive an email warning them. So if a new heart rate is received for a patient that is tachycardic, the email should be sent out at that time.

This code is used locally as the address is 127.0.0.1
We can change it to 0.0.0.0 to receive publicly.

Mine is :  http://vcm-7300.vm.duke.edu:5000/
