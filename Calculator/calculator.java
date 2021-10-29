import java.util.Scanner;

class calculator
{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);

		float a , b, add, sub, mult, div;
		char choice;

 	do 
 	{
		System.out.println("Simple Calculator\n1. Addition \n2. Substraction \n3. Multiplication \n4. Division \n5. Exit \n");

		System.out.println("Enter your choice : ");
		choice = s.next().charAt(0);
		

		switch (choice) 
		{
			case '1':

				System.out.println("Enter first Number : ");
				a = s.nextFloat();
				System.out.println("Enter second Number : ");
				b = s.nextFloat();
				add = a + b ;
				System.out.println(a+" + "+b+" = "+add+"\n");
				break;

			case '2':

				System.out.println("Enter first Number : ");
				a = s.nextFloat();
				System.out.println("Enter second Number : ");
				b = s.nextFloat(); 
				sub = a - b ;
				System.out.println(a+" - "+b+" = "+sub+"\n");
				break;

			case '3':

				System.out.println("Enter first Number : ");
				a = s.nextFloat();
				System.out.println("Enter second Number : ");
				b = s.nextFloat();
				mult = a * b ;
				System.out.println(a+" *"+b+" = "+mult+"\n");
				break;

			case '4':

				System.out.println("Enter first Number : ");
				a = s.nextFloat();
				System.out.println("Enter second Number : ");
				b = s.nextFloat();
				div = a / b ;
				System.out.println(a+" / "+b+" = "+div+"\n");
				break;

			case '5':

				System.exit(0);
				break;
				default:
					System.out.println("Enter correct choice ...... \n");
					break;				
		} 

	}
	
	while (choice!=5); 
	
	}
}
