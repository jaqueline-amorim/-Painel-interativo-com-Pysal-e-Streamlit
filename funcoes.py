import altair as alt

def get_minmax(inputdf,colname,spacing=1):
    descr = inputdf[colname].describe()

    return descr['min']-spacing,descr['max']+spacing


def altair_barchart(inputdf,xfield,yfield='nome'):
    
    return alt.Chart(inputdf).mark_bar().encode(
    x= xfield,
    y=yfield).interactive()