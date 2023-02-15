package main;

import java.lang;

public class TestListADT {

	public static void main(String[] args) {
		// Test our ADT
		
		ListArrayBased aList = new ListArrayBased();
		
		int item1=2;
		
		aList.add(0, item1);
		System.out.println();
		//aList.add(0, 2);
	/*
		for(int i = 0; i <30; i++)
		{
			System.out.println("Size of list is: " + aList.size());
			System.out.println("List: " + aList.toString() + "\n");
			
			try {
				aList.add(i, Integer.valueOf(i));
			}
			catch(ListIndexOutOfBoundsException l)
			{
				System.out.println(l);
			}
		}
		try
		{
			aList.remove(24);
		}
		catch(ListIndexOutOfBoundsException e)
		{
			System.out.println(e);
		}
		
		System.out.println(aList);
		
		try
		{
			aList.add(3,Integer.valueOf(42));
		}
		catch(ListIndexOutOfBoundsException e)
		{
			System.out.println(e);
		}
		System.out.println(aList);
		
		try
		{
			aList.remove(25);
		}
		catch(ListIndexOutOfBoundsException e)
		{
			System.out.println(e);
		}
	*/
	}
}
