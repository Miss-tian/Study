import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
public class File1{
  public static void main(String[] args){
	File file =new File("E:\\yuhengjob\\Newproject\\3#第一卷");
	if (!file.exists()){/*判断文件夹是否存在*/
		file.mkdir();/*新建文件夹*/
	}
	for (int i=1;i<302;i++){
	try{
		BufferedWriter bw=new BufferedWriter(new FileWriter("E:\\yuhengjob\\Newproject\\3#第一卷\\"+i+"#卷more"+i+".txt"));
		bw.write("第"+i+"章"+"\r\n" +"哎，这test废物真是把家族的脸都给丢光了脸都给丢脸都给丢脸都给丢脸都给丢脸都给丢");//向文件中写入内容
		bw.close();//关闭文件
	} catch (IOException e){
		e.printStackTrace();
	}
	}
}
}