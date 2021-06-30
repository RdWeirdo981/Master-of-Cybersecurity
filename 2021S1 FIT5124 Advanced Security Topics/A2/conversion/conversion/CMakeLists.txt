cmake_minimum_required(VERSION 3.10)
project(conversion)
set(NAME "conversion")

find_path(CMAKE_FOLDER NAMES cmake/emp-tool-config.cmake)
include(${CMAKE_FOLDER}/cmake/common.cmake)
include(${CMAKE_FOLDER}/cmake/enable_rdseed.cmake)
include(${CMAKE_FOLDER}/cmake/enable_float.cmake)

set(CMAKE_CXX_STANDARD 14)

find_package(emp-tool REQUIRED)
find_package(emp-ot REQUIRED)
include_directories(${EMP-OT_INCLUDE_DIRS} ${EMP-TOOL_INCLUDE_DIRS})

# Installation
install(FILES cmake/conversion-config.cmake DESTINATION cmake/)
install(DIRECTORY conversion DESTINATION include/)

# Test cases
macro (add_test _name)
    add_test_with_lib(${_name} ${EMP-OT_LIBRARIES} ${EMP-TOOL_LIBRARIES})
endmacro()

add_test(A2Y)
add_test(Y2A)