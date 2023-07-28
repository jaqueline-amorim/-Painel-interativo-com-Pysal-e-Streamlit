
def get_minmax(inputdf,colname,spacing=1):
    descr = inputdf[colname].describe()

    return descr['min']-spacing,descr['max']+spacing