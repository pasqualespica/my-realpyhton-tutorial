# Logging in Python

https://realpython.com/python-logging/

By default, there are 5 standard levels indicating the severity of events. Each has a corresponding method that can be used to log events at that level of severity. The defined levels, in order of increasing severity, are the following:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL


## Basic Configurations
You can use the `basicConfig(**kwargs)` method to configure the logging:

*“You will notice that the logging module breaks PEP8 styleguide and uses camelCase naming conventions. This is because it was adopted from Log4j, a logging utility in Java. It is a known issue in the package but by the time it was decided to add it to the standard library, it had already been adopted by users and changing it to meet PEP8 requirements would cause backwards compatibility issues.”*


Some of the commonly used parameters for basicConfig() are the following:

- level: The root logger will be set to the specified severity level.
- filename: This specifies the file.
- filemode: If filename is given, the file is opened in this mode. The default is a, which means - append.
- format: This is the format of the log message.
