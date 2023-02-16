cmake_minimum_required(VERSION 3.5)
project(example)

# Add support for C++11
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  # Services
  "srv/Example.srv"
  DEPENDENCIES 
    builtin_interfaces 
    geometry_msgs 
    std_msgs
)

ament_package()
ament_python_install_package(${PROJECT_NAME})
