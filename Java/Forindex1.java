/*public class Forindex1{
	public static void main(String[] args){
	 int i;
	 int sum = 0;
	 int m = 0;
	 int n = 0;
	 for(i=1;i<=100;i++){
	 	if ((i%2)!=0){
	 		m = i*10 + 3;
	 		sum += m;
	 		System.out.println("m=" + m);

	 	}
	 	else{
	 		n=(i*10+3)*(-1);
	 		sum += n;
	 		System.out.println("n=" + n);

	 	}
	 	
	 }
	 	System.out.println("sum = " + sum);
	}
}*/
public class Forindex1{
	public static void main(String[] args){
		int sum=0;
	
		for(int a=1;a<=100;a++){
				int j=a*10+3;
			if(a%2==0){
				sum=-1*((-1)*sum+j);
			}else{
				sum=sum+j;
			}
		
	}
	System.out.println(sum);
		}
}