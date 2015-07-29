v.overlay ain=wdpa_snapshot_mollweide@rasterized_parks bin=ecoregs_moll@rasterized_parks out=wdpa_ecoregs_or operator='or'

v.db.addcolumn map=wdpa_ecoregs_or lay=1 columns='area2 DOUBLE PRECISION'

v.to.db map=wdpa_ecoregs_or opt='area' colum='area2' un='meters'

v.out.ogr -sce in=wdpa_ecoregs_or dsn=. ty=area

db.out.ogr wdpa_ecoregs_or dsn=wdpa_ecoregs_or.csv format=CSV

db.out.ogr in=wdpa_ecoregs_or dsn=wdpa_ecoregs_or table=wdpa_ecoregs_or.csv

# R #########################

library(rgeos)
library(rgdal)

parkdir = "parks/"
ecodir = "ecoregions/"

if (!exists("ecoregions")) {
  shpfiles = list.files(ecodir, pattern = "shp")
  shpfiles = strsplit(shpfiles, ".shp")
  if (length(shpfiles) > 1) {
    warning(paste("several shapefiles found in directory", ecodir, "using", shpfiles[[1]]))
  }
  shpfile = shpfiles[[1]]
  ecoregions = readOGR(ecodir,shpfile) 
}
if (!exists("parks")) {
  shpfiles = list.files(parkdir, pattern = "shp")
  shpfiles = strsplit(shpfiles, ".shp")
  if (length(shpfiles) > 1) {
    warning(paste("several shapefiles found in directory", parkdir, "using", shpfiles[[1]]))
  }
  shpfile = shpfiles[[1]]
  parks = readOGR(parkdir,shpfile) 
}  

gIntersection(parks,ecoregions)->park_ecoregs

# R loop #########################

library(rgeos)
library(rgdal)

parkdir = "parks/"
ecodir = "ecoregions/"

if (!exists("ecoregions")) {
  shpfiles = list.files(ecodir, pattern = "shp")
  shpfiles = strsplit(shpfiles, ".shp")
  if (length(shpfiles) > 1) {
    warning(paste("several shapefiles found in directory", ecodir, "using", shpfiles[[1]]))
  }
  shpfile = shpfiles[[1]]
  ecoregions = readOGR(ecodir,shpfile) 
}
if (!exists("parks")) {
  shpfiles = list.files(parkdir, pattern = "shp")
  shpfiles = strsplit(shpfiles, ".shp")
  if (length(shpfiles) > 1) {
    warning(paste("several shapefiles found in directory", parkdir, "using", shpfiles[[1]]))
  }
  shpfile = shpfiles[[1]]
  parks = readOGR(parkdir,shpfile) 
}  

gIntersects(ecoregions,parks,byid=T)->ep # matrix

# calculations ##########################################################

ecoperpa<-function(){

dim(ep)[2]->le

r<-0
data.frame(matrix(NA,nrow=1,ncol=3))->>results
names(results)<<-c('wdpa_id','eco_id','percentage')

for (e in 1:le){

length(which(ep[,e]))->lp

if(lp>0){

parks$WDPA_ID[which(ep[,e])]->pas

for (p in 1:lp){

r<-r+1

# Example showing the parks related to the 3rd ecoregion
#plot(ecoregions[3,])
#plot(parks[ep[,3],],add=T,col='red')

try(gIntersection(ecoregions[e,],parks[which(ep[,e])[p],])->ppee)

#plot(p1e3,col='red')
#plot(parks[which(ep[,3])[1],],add=T)
#plot(ecoregions[3,],add=T)

try(gArea(parks[which(ep[,e])[p],])->app)
try(gArea(ppee)->appee)
try(per_ep<-100*appee/app)

try(results[r,]<<-c(pas[p],ecoregions$eco_id[e],per_ep))
print(paste('row:',r))
# add a try for ecoregions without parks


}
ppee<-NULL # last added
app<-NULL # last added
appee<-NULL # last added
per_ep<-NULL # last added

print(paste('PA',p))
}
print(paste('ECO',e))
}
write.table(results,'results.csv',row.names=F,sep=';')
print('END')
}

# calculations ##########################################################

out <- lapply(which(ep[,i]),function(x){ gIntersection(ecoregion[i,],parks[ep[x,i],])})

gIntersection(parks[1,],ecoregions[which(p1i),])->p1_inter

gI <- gIntersects( WorldMap , clip.extent , byid = TRUE )
out <- lapply( which(gI) , function(x){ gIntersection( WorldMap[x,] , clip.extent ) } )



