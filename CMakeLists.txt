cmake_minimum_required(VERSION 2.8)
Project("proj1")

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/_cmake")
include(_cmake/config.cmake)
include(_cmake/dependencies.cmake)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_subdirectory(proj1)
