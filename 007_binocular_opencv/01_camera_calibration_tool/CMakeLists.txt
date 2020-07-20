cmake_minimum_required(VERSION 3.15)

# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fvisibility=hidden -DEIGEN_MAX_ALIGN_BYTES=32 -DEIGEN_DONT_VECTORIZE -fPIC -march=native -DGPU -DCUDNN -DOPENCV -g -std=c++11 -W -O3 -pthread -DS_DEBUG")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fvisibility=hidden -DEIGEN_MAX_ALIGN_BYTES=32 -DEIGEN_DONT_VECTORIZE -fPIC -march=native -DGPU -DCUDNN -DOPENCV -g -std=c++11 -pthread")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}  -fvisibility=hidden -DGPU -DCUDNN -DOPENCV -g -std=c++11 -fPIC ")  # 编译C脚本时调用GPU环境信息

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Debug")
endif()

set(CMAKE_CXX_FLAGS_DEBUG "-fopenmp -w -g -O0 ${CMAKE_CXX_FLAGS}")
set(CMAKE_C_FLAGS_DEBUG "-fopenmp -w -g -O0 ${CMAKE_C_FLAGS}")

set(CMAKE_CXX_FLAGS_RELEASE "-fopenmp -w -O3 ${CMAKE_CXX_FLAGS}")
set(CMAKE_C_FLAGS_RELEASE "-fopenmp -w -O3 ${CMAKE_C_FLAGS}")

project(activate)
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/build)
set(CMAKE_CXX_STANDARD 11)
add_compile_options(-fPIC -ldl -lm -g -Wall  -Wshadow -Wno-sign-compare -w)

file(GLOB_RECURSE CURRENT_HEADERS
        ./*.h
)

# 检索查找文件信息
file(GLOB sources
        ./*.cpp
)

source_group("Include" FILES ${CURRENT_HEADERS})
source_group("Source" FILES ${sources})

SET(LIBS
        opencv_core
        opencv_highgui
        opencv_imgcodecs
        opencv_imgproc
        opencv_xfeatures2d
        opencv_features2d
        opencv_cudafeatures2d
        opencv_stitching
        opencv_calib3d
        opencv_videoio
        opencv_video
        opencv_flann
        opencv_cudaimgproc
        opencv_cudalegacy
        stdc++fs  #设置-lstdc++fs 新链接器选项，防止std等gcc库调用不到
        jsoncpp
        cudart
        vl
        )

set(opencvdir /home/disk1/s_opt/opencv/opencv3.4.8)

include_directories(".")
include_directories(${opencvdir}/include/)
include_directories(/usr/include)

link_directories(${opencvdir}/lib)
link_directories(/home/disk1/s_opt/vlfeat/bin/glnxa64)
link_directories(/usr/local/lib/)
link_directories(/usr/lib/x86_64-linux-gnu/)  #动态链接库目录/bazel-bin/tensorflow


#添加要编译的可执行文件
cuda_add_executable(${PROJECT_NAME}
        main.cpp
        ${sources}
        ${CURRENT_HEADERS}
        )

#cuda_add_library(${PROJECT_NAME} SHARED ${sources}  ${CURRENT_HEADERS})

#设置 target 需要链接的库
#添加可执行文件所需要的库,连接libtensorflow_cc.so和libtensorflow_framework库，链接动态链接库
target_link_libraries(${PROJECT_NAME}
        ${LIBS}
        )