#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#This file is for test purpose only ! Donot use it commercially#
# Again for testing purpose
# More changes in the file 
#Much more changes to file
class xyz:
    def __init__(self,length,breadth):
        self.length = length;
        self.breadth = breadth;
        
    def area(self,):
        return(self.length*self.breadth);
        
        
def main():
    r = xyz(10,20);
    print(r.area());
if __name__ == "__main__":main()
