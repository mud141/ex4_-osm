def save_osm(osm_handler,osm_type,save_path=r"./data/",fileType="GPKG"):
    import geopandas as gpd
    import os
    import datetime
    
    a_T=datetime.datetime.now()
    print("start time:",a_T)    
    
    '''
    function-根据条件逐个保存读取的osm数据（node, way and area）
    
    Paras:
    osm_handler - osm返回的node,way和area数据
    osm_type - 要保存的osm元素类型
    save_path - 保存路径
    fileType - 保存的数据类型，shp, GeoJSON, GPKG
    '''
    def duration(a_T):
        b_T=datetime.datetime.now()
        print("end time:",b_T)
        duration=(b_T-a_T).seconds/60
        print("Total time spend:%.2f minutes"%duration)
        
    def save_gdf(osm_node_gdf,fileType,osm_type):
        if fileType=="GeoJSON":
            osm_node_gdf.to_file(os.path.join(save_path,"osm_%s.geojson"%osm_type),driver='GeoJSON')
        elif fileType=="GPKG":
            osm_node_gdf.to_file(os.path.join(save_path,"osm_%s.gpkg"%osm_type),driver='GPKG')
        elif fileType=="shp":
            osm_node_gdf.to_file(os.path.join(save_path,"osm_%s.shp"%osm_type))

    crs={'init': 'epsg:4326'} #配置坐标系统，参考：https://spatialreference.org/        
    osm_columns=['type','geometry','id','version','visible','ts','uid','user','changeet','tagLen','tags']
    if osm_type=="node":
        osm_node_gdf=gpd.GeoDataFrame(osm_handler.osm_node,columns=osm_columns,crs=crs)
        save_gdf(osm_node_gdf,fileType,osm_type)
        duration(a_T)
        return osm_node_gdf

    elif osm_type=="way":
        osm_way_gdf=gpd.GeoDataFrame(osm_handler.osm_way,columns=osm_columns,crs=crs)
        save_gdf(osm_way_gdf,fileType,osm_type)
        duration(a_T)
        return osm_way_gdf
        
    elif osm_type=="area":
        osm_area_gdf=gpd.GeoDataFrame(osm_handler.osm_area,columns=osm_columns,crs=crs)
        save_gdf(osm_area_gdf,fileType,osm_type)
        duration(a_T)
        return osm_area_gdf

node_gdf=save_osm(osm_handler,osm_type="node",save_path=r"./data/",fileType="GPKG")

way_gdf=save_osm(osm_handler,osm_type="way",save_path=r"./data/",fileType="GPKG")

area_gdf=save_osm(osm_handler,osm_type="area",save_path=r"./data/",fileType="GPKG")


