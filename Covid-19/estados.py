#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import  codecs
import csv

archivoEstados = "201111COVID19MEXICO.csv"

datosUTF = codecs.open(archivoEstados,'r','utf-8',errors='ignore')
df = pd.read_csv(datosUTF)

for i,j in df.groupby(["ENTIDAD_RES","MUNICIPIO_RES"]):
    j.to_csv('{}.csv'.format(i),index=False)


