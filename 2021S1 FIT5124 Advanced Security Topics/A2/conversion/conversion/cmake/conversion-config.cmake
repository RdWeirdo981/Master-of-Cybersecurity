find_package(emp-ot)

find_path(CONVERSION_INCLUDE_DIR conversion/conversion.h)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(conversion DEFAULT_MSG CONVERSION_INCLUDE_DIR)

if(CONVERSION_FOUND)
    set(CONVERSION_INCLUDE_DIRS ${EMP-TOOL_INCLUDE_DIR} ${EMP-OT_INCLUDE_DIRS})
    set(CONVERSION_LIBRARIES ${EMP-TOOL_LIBRARIES})
endif()
