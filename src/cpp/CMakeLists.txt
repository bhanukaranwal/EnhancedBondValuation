cmake_minimum_required(VERSION 3.10)
project(EnhancedBondValuationCpp)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find necessary libraries
find_package(Boost REQUIRED)
find_package(Eigen3 REQUIRED)
# find_package(CURL REQUIRED) # Uncomment when api_integration is implemented

# Include directories
include_directories(include)
include_directories(${Boost_INCLUDE_DIRS})
include_directories(${EIGEN3_INCLUDE_DIR})

# Add the main library (can be STATIC or SHARED)
add_library(bond_lib STATIC
    bond_calculator.cpp
    yield_solver.cpp
    monte_carlo.cpp
)

# --- Test Suite ---
enable_testing()

# Add test executable
add_executable(test_suite tests/main_test.cpp tests/test_bond_calculator.cpp)

# Link libraries to the test suite
target_link_libraries(test_suite PRIVATE bond_lib)

# Add test to CTest
add_test(NAME CppUnitTests COMMAND test_suite)
