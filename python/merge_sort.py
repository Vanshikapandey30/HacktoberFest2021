{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 CourierNewPS-BoldMT;\f1\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red244\green0\blue95;\red29\green30\blue26;\red255\green255\blue255;
\red246\green246\blue239;\red88\green209\blue235;\red157\green101\blue255;\red98\green94\blue76;\red224\green213\blue97;
}
{\*\expandedcolortbl;;\cssrgb\c97647\c14902\c44706;\cssrgb\c15294\c15686\c13333;\cssrgb\c100000\c100000\c100000;
\cssrgb\c97255\c97255\c94902;\cssrgb\c40000\c85098\c93725;\cssrgb\c68235\c50588\c100000;\cssrgb\c45882\c44314\c36863;\cssrgb\c90196\c85882\c45490;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl352\partightenfactor0

\f0\b\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 mergeSort(arr):
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \'a0\'a0\'a0\'a0
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 if
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf6 \strokec6 len\cf5 \strokec5 (arr) > \cf7 \strokec7 1\cf5 \strokec5 :
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf8 \strokec8 # Finding the mid of the array
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 mid 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf6 \strokec6 len\cf5 \strokec5 (arr)
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 //
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7 2
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf8 \strokec8 # Dividing the array elements
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 L 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 arr[:mid]
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf8 \strokec8 # into 2 halves
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 R 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 arr[mid:]
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf8 \strokec8 # Sorting the first half
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 mergeSort(L)
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf8 \strokec8 # Sorting the second half
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 mergeSort(R)
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 i 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 j 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 k 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7 0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf8 \strokec8 # Copy data to temp arrays L[] and R[]
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 while
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 i < \cf6 \strokec6 len\cf5 \strokec5 (L) 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 and
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 j < \cf6 \strokec6 len\cf5 \strokec5 (R):
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 if
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 L[i] < R[j]:
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 arr[k] 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 L[i]
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 i 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 +=
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7 1
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 else
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 :
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 arr[k] 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 R[j]
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 j 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 +=
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7 1
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 k 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 +=
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7 1
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf8 \strokec8 # Checking if any element was left
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 while
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 i < \cf6 \strokec6 len\cf5 \strokec5 (L):
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 arr[k] 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 L[i]
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 i 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 +=
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7 1
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 k 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 +=
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7 1
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 while
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 j < \cf6 \strokec6 len\cf5 \strokec5 (R):
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 arr[k] 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 R[j]
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 j 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 +=
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7 1
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf5 \strokec5 k 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 +=
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf7 \strokec7 1
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\
\pard\pardeftab720\sl352\partightenfactor0

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf8 \strokec8 # Code to print the list
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\
\pard\pardeftab720\sl352\partightenfactor0

\f0\b\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 def
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 printList(arr):
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \'a0\'a0\'a0\'a0
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 for
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 i 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 in
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf6 \strokec6 range\cf5 \strokec5 (\cf6 \strokec6 len\cf5 \strokec5 (arr)):
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 print
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 (arr[i], end
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf9 \strokec9 " "\cf5 \strokec5 )
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\cf6 \strokec6 print\cf5 \strokec5 ()
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \'a0\
\pard\pardeftab720\sl352\partightenfactor0

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf8 \strokec8 # Driver Code
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0

\f0\b\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 if
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 __name__ 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 ==
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf9 \strokec9 '__main__'\cf5 \strokec5 :
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \
\pard\pardeftab720\sl352\partightenfactor0

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \'a0\'a0\'a0\'a0\cf5 \strokec5 arr 
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4  
\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 [\cf7 \strokec7 12\cf5 \strokec5 , \cf7 \strokec7 11\cf5 \strokec5 , \cf7 \strokec7 13\cf5 \strokec5 , \cf7 \strokec7 5\cf5 \strokec5 , \cf7 \strokec7 6\cf5 \strokec5 , \cf7 \strokec7 7\cf5 \strokec5 ]
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\cf6 \strokec6 print\cf5 \strokec5 (\cf9 \strokec9 "Given array is"\cf5 \strokec5 , end
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf9 \strokec9 "\\n"\cf5 \strokec5 )
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\cf5 \strokec5 printList(arr)
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\cf5 \strokec5 mergeSort(arr)
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 print
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf5 \strokec5 (\cf9 \strokec9 "Sorted array is: "\cf5 \strokec5 , end
\f0\b \AppleTypeServices\AppleTypeServicesF65539 \cf2 \strokec2 =
\f1\b0 \AppleTypeServices\AppleTypeServicesF65539 \cf9 \strokec9 "\\n"\cf5 \strokec5 )
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \

\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \'a0\'a0\'a0\'a0\cf5 \strokec5 printList(arr)
\fs24 \AppleTypeServices\AppleTypeServicesF65539 \cf4 \strokec4 \
}