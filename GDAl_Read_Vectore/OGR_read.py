# AI_Javaher
# this is the first session of GDAL/OGR tutorial
# install GDAL video : https://www.youtube.com/watch?v=YsdHWT-hA4k&list=PLFhf3UaNX_xc8ivjt773rAjGNoAfz_ELm&index=2
# check the video of this code in youtube :https://www.youtube.com/watch?v=F1jaX9vmhIk
# you can find the list of videos about GDAL tutorial in link : https://www.youtube.com/playlist?list=PLFhf3UaNX_xc8ivjt773rAjGNoAfz_ELm
# you can find more videos about artificial intelligence in : https://www.youtube.com/channel/UCxKMssgH5eai60XeIuvg-dg
########################## GDAL_Read vector ##########################
from osgeo import ogr

mnh_shp = ogr.Open('D:\\youtube\\GDAL\\GDAL_introduction\\data\\manhattan\\manhattan_zone.shp',0)
mnh_lyr = mnh_shp.GetLayer(0)
mnh_feature_num = mnh_lyr.GetFeatureCount()
# print(mnh_feature_num)
mnh_feature = mnh_lyr.GetFeature(0)
# print(mnh_feature.zone)
# print(mnh_feature.LocationID)
mnh_feature_last = mnh_lyr.GetFeature(mnh_feature_num-1)
# print(mnh_feature_last.LocationID,'last')
for f in mnh_lyr:
    # print(f.zone)
    geo = f.geometry()
    print(geo)
