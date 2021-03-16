# -*- coding: utf-8 -*-
"""
March Madness Analysis
Steven Lucas & Sejin Kim
STAT 306 S21 @ Kenyon College

RDS-specific function definitions
"""

class rdshandling:
    def getfilename(url = ''):
        '''
        Get the strict filename or indexed directory from a URL
    
        Parameters
        ----------
        url : string
            The URL to extract the filename from. The default is ''.
    
        Returns
        -------
        string
            The extracted filename from the URL.
    
        '''
        fragmentRemoved = url.split("#")[0]
        queryStringRemoved = fragmentRemoved.split("?")[0]
        schemeRemoved = queryStringRemoved.split("://")[-1].split(":")[-1]
        if schemeRemoved.find("/") == -1:
            return ''
        return path.basename(schemeRemoved)
        
    def readremoteRDSdata(url = ''):
        """
        Read an R RDS file from a remote Internet repository by URL
    
        Parameters
        ----------
        url : string
            The raw-formatted RDS file to load in. The default is ''.
    
        Raises
        ------
        Exception
            Throws an exception if scratch disk is unavailable or data is inaccessible.
    
        Returns
        -------
        pandas dataframe
            A pandas dataframe that has the uncompressed data from the URL..
    
        """
        scratch = ''
        try:
            scratch = getfilename(url) + '.rda'
        except:
            raise Exception("Random filename issue")
        local = None
        result = None
        try:
            local = pyreadr.download_file(url, scratch)
            result = pyreadr.read_r(local)
        except Exception as e:
            print(e)
            raise Exception("Inaccessible URL")
        return result[None]