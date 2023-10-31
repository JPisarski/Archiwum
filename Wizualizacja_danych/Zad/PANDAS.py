# import pandas as pd
# import numpy as np
# import openpyxl as pl
# import datetime as dt
#
#
# #zadanie 1
#
# x = pd.read_excel("imiona.xlsx", header=0)
# print(x)
#
# # zadanie 2
#
# print(x[x["Liczba"]>1000])
#
# print(x[x["Imie"]=="JAKUB"])
#
# print("Liczba wszystkich urodzonych dzieci w całym okresie:")
# print(x["Liczba"].sum())
#
# y = x[(x["Rok"]>=2000) & (x["Rok"]<=2005)]
# print(y)
# print("Suma dzieci urodzonych w latach 2000-2005:")
# print(y["Liczba"].sum())
#
# chłopcy = x[x["Plec"]=="M"]
# print("Suma urodzonych chłopców:")
# print(chłopcy["Liczba"].sum())
# dziewczynki = x[x["Plec"]=="K"]
# print("Suma urodzonych dziewczynek:")
# print(dziewczynki["Liczba"].sum())
#
#
# z2000 = chłopcy[chłopcy["Rok"]==2000]
# z2000_f = z2000[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2000 roku:")
# print(z2000_f.idxmax().iloc[0])
# z2001 = chłopcy[chłopcy["Rok"]==2001]
# z2001_f = z2001[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2001 roku:")
# print(z2001_f.idxmax().iloc[0])
# z2002 = chłopcy[chłopcy["Rok"]==2002]
# z2002_f = z2002[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2002 roku:")
# print(z2002_f.idxmax().iloc[0])
# z2003 = chłopcy[chłopcy["Rok"]==2003]
# z2003_f = z2003[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2003 roku:")
# print(z2003_f.idxmax().iloc[0])
# z2004 = chłopcy[chłopcy["Rok"]==2004]
# z2004_f = z2004[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2004 roku:")
# print(z2004_f.idxmax().iloc[0])
# z2005 = chłopcy[chłopcy["Rok"]==2005]
# z2005_f = z2005[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2005 roku:")
# print(z2005_f.idxmax().iloc[0])
# z2006 = chłopcy[chłopcy["Rok"]==2006]
# z2006_f = z2006[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2006 roku:")
# print(z2006_f.idxmax().iloc[0])
# z2007 = chłopcy[chłopcy["Rok"]==2007]
# z2007_f = z2007[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2007 roku:")
# print(z2007_f.idxmax().iloc[0])
# z2008 = chłopcy[chłopcy["Rok"]==2008]
# z2008_f = z2008[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2008 roku:")
# print(z2008_f.idxmax().iloc[0])
# z2009 = chłopcy[chłopcy["Rok"]==2009]
# z2009_f = z2009[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2009 roku:")
# print(z2009_f.idxmax().iloc[0])
# z2010 = chłopcy[chłopcy["Rok"]==2010]
# z2010_f = z2010[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2010 roku:")
# print(z2010_f.idxmax().iloc[0])
# z2011 = chłopcy[chłopcy["Rok"]==2011]
# z2011_f = z2011[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2011 roku:")
# print(z2011_f.idxmax().iloc[0])
# z2012 = chłopcy[chłopcy["Rok"]==2012]
# z2012_f = z2012[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2012 roku:")
# print(z2012_f.idxmax().iloc[0])
# z2013 = chłopcy[chłopcy["Rok"]==2013]
# z2013_f = z2013[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2013 roku:")
# print(z2013_f.idxmax().iloc[0])
# z2014 = chłopcy[chłopcy["Rok"]==2014]
# z2014_f = z2014[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2014 roku:")
# print(z2014_f.idxmax().iloc[0])
# z2015 = chłopcy[chłopcy["Rok"]==2015]
# z2015_f = z2015[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2015 roku:")
# print(z2015_f.idxmax().iloc[0])
# z2016 = chłopcy[chłopcy["Rok"]==2016]
# z2016_f = z2016[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2016 roku:")
# print(z2016_f.idxmax().iloc[0])
# z2017 = chłopcy[chłopcy["Rok"]==2017]
# z2017_f = z2017[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię męskie w 2017 roku:")
# print(z2017_f.idxmax().iloc[0])
# z2000 = dziewczynki[dziewczynki["Rok"]==2000]
# z2000_k = z2000[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2000 roku:")
# print(z2000_k.idxmax().iloc[0])
# z2001 = dziewczynki[dziewczynki["Rok"]==2001]
# z2001_k = z2001[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2001 roku:")
# print(z2001_k.idxmax().iloc[0])
# z2002 = dziewczynki[dziewczynki["Rok"]==2002]
# z2002_k = z2002[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2002 roku:")
# print(z2002_k.idxmax().iloc[0])
# z2003 = dziewczynki[dziewczynki["Rok"]==2003]
# z2003_k = z2003[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2003 roku:")
# print(z2003_k.idxmax().iloc[0])
# z2004 = dziewczynki[dziewczynki["Rok"]==2004]
# z2004_k = z2004[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2004 roku:")
# print(z2004_k.idxmax().iloc[0])
# z2005 = dziewczynki[dziewczynki["Rok"]==2005]
# z2005_k = z2005[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2005 roku:")
# print(z2005_k.idxmax().iloc[0])
# z2006 = dziewczynki[dziewczynki["Rok"]==2006]
# z2006_k = z2006[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2006 roku:")
# print(z2006_k.idxmax().iloc[0])
# z2007 = dziewczynki[dziewczynki["Rok"]==2007]
# z2007_k = z2007[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2007 roku:")
# print(z2007_k.idxmax().iloc[0])
# z2008 = dziewczynki[dziewczynki["Rok"]==2008]
# z2008_k = z2008[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2008 roku:")
# print(z2008_k.idxmax().iloc[0])
# z2009 = dziewczynki[dziewczynki["Rok"]==2009]
# z2009_k = z2009[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2009 roku:")
# print(z2009_k.idxmax().iloc[0])
# z2010 = dziewczynki[dziewczynki["Rok"]==2010]
# z2010_k = z2010[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2010 roku:")
# print(z2010_k.idxmax().iloc[0])
# z2011 = dziewczynki[dziewczynki["Rok"]==2011]
# z2011_k = z2011[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2011 roku:")
# print(z2011_k.idxmax().iloc[0])
# z2012 = dziewczynki[dziewczynki["Rok"]==2012]
# z2012_k = z2012[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2012 roku:")
# print(z2012_k.idxmax().iloc[0])
# z2013 = dziewczynki[dziewczynki["Rok"]==2013]
# z2013_k = z2013[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2013 roku:")
# print(z2013_k.idxmax().iloc[0])
# z2014 = dziewczynki[dziewczynki["Rok"]==2014]
# z2014_k = z2014[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2014 roku:")
# print(z2014_k.idxmax().iloc[0])
# z2015 = dziewczynki[dziewczynki["Rok"]==2015]
# z2015_k = z2015[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2015 roku:")
# print(z2015_k.idxmax().iloc[0])
# z2016 = dziewczynki[dziewczynki["Rok"]==2016]
# z2016_k = z2016[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2016 roku:")
# print(z2016_k.idxmax().iloc[0])
# z2017 = dziewczynki[dziewczynki["Rok"]==2017]
# z2017_k = z2017[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print("Najpopularniejsze imię żeńskie w 2017 roku:")
# print(z2017_k.idxmax().iloc[0])
#
#
# f = chłopcy[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print(f)
# print("Najpopularniejsze imię męskie w całym okresie:")
# print(f.idxmax().iloc[0])
# k = dziewczynki[["Imie","Liczba"]].groupby(["Imie"]).agg({"Liczba":["sum"]})
# print(k)
# print("Najpopularniejsze imię żeńskie w całym okresie:")
# print(k.idxmax().iloc[0])
#
# #zadanie 3
#
# w = pd.read_csv("zamowienia.csv", header=0, sep=";", decimal=".")
#
# print(w["Sprzedawca"].unique())
#
# print(w["Utarg"].sort_values(ascending=False).head(5))
#
# print(w[["Sprzedawca","idZamowienia"]].groupby(["Sprzedawca"]).agg({"idZamowienia":["count"]}))
#
# print(w[["Kraj","idZamowienia"]].groupby(["Kraj"]).agg({"idZamowienia":["count"]}))
#
# m = w[(w["Kraj"]=="Polska") & (pd.to_datetime(w["Data zamowienia"]).dt.year==2005)]
# print(m.agg({"idZamowienia":["count"]}))
#
# n = w[pd.to_datetime(w["Data zamowienia"]).dt.year==2004]
# print(n.agg({"Utarg":["mean"]}))
#
# n.to_csv("zamowienia_2004.csv", index=False)
# o = w[pd.to_datetime(w["Data zamowienia"]).dt.year==2005]
# o.to_csv("zamowienia_2005.csv", index=False)
#



