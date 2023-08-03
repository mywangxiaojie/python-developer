# 案例：使用OpenCV的GrapCut实现有用户交互的抠图

# grabCut( InputArray img, InputOutputArray mask, Rect rect,
#                            InputOutputArray bgdModel, InputOutputArray fgdModel,
#                            int iterCount, int mode = GC_EVAL );

#     img --> 输入的三通道图像；
#     mask --> 输入的单通道图像，初始化方式为GC_INIT_WITH_RECT表示ROI区域可以被初始化为：
#     GC_BGD --> 定义为明显的背景像素 0
#     GC_FGD --> 定义为明显的前景像素 1
#     GC_PR_BGD --> 定义为可能的背景像素 2
#     GC_PR_FGD --> 定义为可能的前景像素 3
#     rect --> 表示roi区域；
#     bgdModel --> 表示临时背景模型数组；
#     fgdModel --> 表示临时前景模型数组；
#     iterCount --> 表示图割算法迭代次数, 次数越多，效果越好；
#     mode --> 当使用用户提供的roi时候使用GC_INIT_WITH_RECT

# 实现算法的步骤：

# 　　　　1.创建一个遮罩，并初始化为背景GC_BGD

# 　　　　2.用户选定一个ROI区域初始化为前景GC_FGD

# 　　　　3.调用grabCut函数实现算法

# 　　　　4.输入mask即为目标抠图

# 参考代码：
# CrabCut_Matting::CrabCut_Matting(QWidget *parent)
#     : MyGraphicsView{parent}
# {
#     this->setWindowTitle("crabCut抠图");
#     this->setMouseTracking(true);//设置鼠标事件可用
#     init = false;
#     numRun = false;
# }


# void CrabCut_Matting::dropEvent(QDropEvent*event){
#     QString filePath = event->mimeData()->urls().at(0).toLocalFile();
#     showCrabCutMatting(filePath.toStdString().c_str());
# }

# void CrabCut_Matting::showCrabCutMatting(const char* filePath){
#     src = imread(filePath);
#     if(src.empty()){
#         qDebug()<<"输入图像为空";
#         return;
#     }

#     //创建一个背景遮罩
#     mMask = Mat::zeros(src.size(),CV_8UC1);
#     mMask.setTo(Scalar::all(GC_BGD));


#     convert2Sence(src);
# }
# void CrabCut_Matting::mouseMoveEvent(QMouseEvent *event){
#     //    if(event->button()==Qt::LeftButton){//鼠标左键
#     rect = Rect(Point(rect.x, rect.y), Point(event->pos().x(), event->pos().y()));
#     qDebug()<<"mouseMoveEvent:"<<rect.width<<"|"<<rect.height;
#     showImage();
#     //    }
# }

# void CrabCut_Matting::mousePressEvent(QMouseEvent *event){
#     grabMouse();
#     if(event->button()==Qt::LeftButton){//鼠标左键
#         rect.x = event->pos().x();
#         rect.y = event->pos().y();
#         rect.width = 1;
#         rect.height = 1;
#         init = false;
#         numRun = 0;
#         qDebug()<<"mousePressEvent:"<<event->pos().x()<<"|"<<event->pos().y();
#     }

# }

# void CrabCut_Matting::mouseReleaseEvent(QMouseEvent *event){
#     releaseMouse();
#     if(event->button()==Qt::LeftButton){//鼠标左键
#         if (rect.width > 1 && rect.height > 1) {
#             setROIMask();
#             qDebug()<<"mouseReleaseEvent:"<<rect.width<<"|"<<rect.height;
#             //执行grabcut的代码
#             runGrabCut();
#             numRun++;
#             showImage();
#         }

#     }
# }
# /**
#  * 将选中的区域设置为前景
#  * @brief CrabCut_Matting::setROIMask
#  */
# void CrabCut_Matting::setROIMask(){
#     // GC_FGD = 1
#     // GC_BGD =0;
#     // GC_PR_FGD = 3
#     // GC_PR_BGD = 2
#     mMask.setTo(GC_BGD);
#     rect.x = max(0, rect.x);
#     rect.y = max(0, rect.y);
#     rect.width = min(rect.width, src.cols - rect.x);
#     rect.height = min(rect.height, src.rows - rect.y);
#     mMask(rect).setTo(Scalar(GC_PR_FGD));//将选中的区域设置为
# }

# void CrabCut_Matting::showImage(){
#     Mat result, binMask;
#     binMask.create(mMask.size(), CV_8UC1);
#     binMask = mMask & 1;
#     if (init) {
#         src.copyTo(result, binMask);
#     } else {
#         src.copyTo(result);
#     }
#     rectangle(result, rect, Scalar(0, 0, 255), 2, 8);
#     convert2Sence(result);

# }


# void CrabCut_Matting::runGrabCut(){
#     if (rect.width < 2 || rect.height < 2) {
#         return;
#     }

#     if (init) {
#         grabCut(src, mMask, rect, bgModel, fgModel, 1);
#     } {
#         grabCut(src, mMask, rect, bgModel, fgModel, 1, GC_INIT_WITH_RECT);
#         init = true;
#     }
# }


# void CrabCut_Matting::convert2Sence(Mat target){
#     scene.clear();
#     QImage image = ImageUtils::matToQImage(target);
#     QPixmap pixmap = QPixmap::fromImage(image);
#     QGraphicsPixmapItem *item = new QGraphicsPixmapItem(pixmap.scaled(this->size(),Qt::KeepAspectRatio,Qt::SmoothTransformation));
#     scene.addItem(item);
# }


# 参考以上代码，用python实现