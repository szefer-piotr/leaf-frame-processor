
setwd("C:/Users/Katerina Sam/Desktop/Central_Brain/Exclosure_Experiments/BEBA_2014_FirstPatrol/Leaf_frames_work/Leaf_frame_photos/Finished_200/All_Summarized") 
axls<-list.files(".",pattern = "*.xls")
myres<-data.frame(Label=NA,XStart=NA,YStart=NA,Area.x=NA,Area.y=NA)
for(f in axls){ # f=axls[1]
  of<- read.csv(f,sep="\t")
  half<-dim(of)[1]  
  myres<- rbind(myres,merge(
    of[1:(half/2),c(2,3,grep("Start",names(of)))],
    of[((half/2)+1):half,c(2,3,grep("Start",names(of)))],
    by=c("Label","XStart","YStart")) )
  
}
myres$Herbivory<-myres$Area.x-myres$Area.y
write.table(myres[-c(1),],"2FINALareas.csv",row.names=F)
