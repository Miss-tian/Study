import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
public class File1{
  public static void main(String[] args){
	File file =new File("E:\\yuhengjob\\Newproject\\1000���½ڵĴ��½�С˵");
	if (!file.exists()){/*�ж��ļ����Ƿ����*/
		file.mkdir();/*�½��ļ���*/
	}
	for (int i=1;i<1001;i++){
	try{
		BufferedWriter bw=new BufferedWriter(new FileWriter("E:\\yuhengjob\\Newproject\\1000���½ڵĴ��½�С˵\\"+i+"#��more"+i+".txt"));
		bw.write("��"+i+"��"+"\r\n" +"������������ǰѼ������sdfd��������s������������������������������������������");//���ļ���д������
		bw.close();//�ر��ļ�
	} catch (IOException e){
		e.printStackTrace();
	}
	}
}
}