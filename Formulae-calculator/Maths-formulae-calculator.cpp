//Run it on Turbo C++ or some online compiler
#include <iostream>
#include <conio.h>
#include <math.h>
using namespace std;

struct formulae
{
    int r;
    int i;
    float x;
    float y;
    float z;
};
formulae c1,c2,c3,p1,p2,p3,p4;

int main()
{
    clrscr();
    cout<<"                         \n\nFORMULAE LIST:\n\n";
    cout<<"1 for ADDITION OF COMPLEX NUMBERS \n";
    cout<<"2 for ROOTS OF QUADRATIC EQUATION\n";
    cout<<"3 for FACTORIAL OF A NUMBER\n";
    cout<<"4 for ARITHMETIC AND GEOMETRIC PROGRESSION\n";
    cout<<"5 for SLOPE OF A LINE\n";
    cout<<"6 for COLLINEARITY OF THREE POINTS\n";
    cout<<"7 for 3 - D GEOMETRY\n\n";
    cout<<"Enter the number of chapter you want to solve using formulae - ";
    int ch;
    cin>>ch;
    clrscr();

    if(ch==1)
    {
        cout<<"                         \n\nADDITION OF COMPLEX NUMBERS\n\n";
        cout<<"Enter the real and imaginary part of 1st number\n";
        cin>>c1.r>>c1.i;
        cout<<"Enter the real and imaginary part of 2nd number\n";
        cin>>c2.r>>c2.i;
        c3.r=c1.r+c2.r;
        c3.i=c1.i+c2.i;
        cout<<"Result = "<<c3.r<<" + i"<<c3.i;
    }


    else if(ch==2)
    {
        int a,b,c,x,y;
        cout<<"                         \n\nROOTS OF QUADRATIC EQUATION\n";
        cout<<"Enter the coefficient of ax^2 + bx+ c from the equation \n";
        cin>>a>>b>>c;
        x=(-b+(sqrt((b*b)-4*a*c)))/(2*a);
        y=(-b-(sqrt((b*b)-4*a*c)))/(2*a);
        cout<<"Value of x = "<<x<<" and "<<y;
    }


    else if(ch==3)
    {
        cout<<"                         \n\nFACTORIAL OF A NUMBER\n\n";
        cout<<"Enter a number to find factorial \n";
        int n,i,fact=1;
        cin>>n;
        i=n;
        while(n)
        {
            fact*=n;
            --n;
        }
        cout<<"The factorial of "<<i<<" is "<<fact<<"\n";
    }


    else if(ch==4)
    {
        cout<<"                         \n\nARITHMETIC AND GEOMETRIC PROGRESSION\n\n";
        cout<<"Enter A to find nth term of an A.P\n";
        cout<<"Enter B to find sum of n terms in A.P.\n";
        cout<<"Enter C to find arithmetic mean in an A.P.\n";
        cout<<"Enter D to find nth term of a G.P.\n";
        cout<<"Enter E to find sum of n terms in G.P.\n";
        cout<<"Enter F to find geometric mean in G.P.\n";
        char c;
        cin>>c;
        clrscr();

        if(c=='A')
        {
            cout<<"                         \n\nnth TERM OF AN A.P.\n\n";
            cout<<"Enter value of a from the given A.P. - ";
            int a;
            cin>>a;
            cout<<"\nEnter value of n - ";
            int n;
            cin>>n;
            cout<<"\nEnter balue of d - ";
            int d;
            cin>>d;
            int an=a+(n-1)*d;
            cout<<n<<" term is "<<an;
        }
        
        else if(c=='B')
        {
        cout<<"                         \n\nSUM OF n TERMS IN A.P.\n\n";
        cout<<"Enter value of a - ";
        int a;
        cin>>a;
        cout<<"Enter value of n - ";
        int n;
        cin>>n;
        cout<<"Enter value of d - ";
        int d;
        cin>>d;
        int p=n/2;
        int q=2*a;
        int r=n-1;
        int s=r*d;
        int sn=p*(q+s);
        cout<<"Sum of "<<n<<" terms of the A.P. is "<<sn;
    }
    
    else if(c=='C')
    {
        cout<<"                         \n\nARITHMETIC MEAN IN AN A.P.\n\n";
        cout<<"Enter 2 numbers a and b to find their Arithmetic mean\n";
        int a,b;
        cin>>a>>b;
        int am=(a+b)/2;
        cout<<"Arithmetic mean of "<<a<<" & "<<b<<" is "<<am<<endl;
        cout<<"Thus A.P. constructed is "<<a<<", "<<am<<", "<<b;
    }
    
    else if(c=='D')
    {
        cout<<"                         \n\nnth TERM IN A G.P\n\n";
        cout<<"Enter value of a for the G.P. - ";
        int a;
        cin>>a;
        cout<<"Enter value of r - ";
        int r;
        cin>>r;
        cout<<"Enter value of n - ";
        int n;
        cin>>n;
        int x=n-1;
        int y=pow(r,x);
        int an=a*y;
        cout<<n<<" term of the G.P. is "<<an;
    }

    else if(c=='E')
    {
        cout<<"                         \n\nSUM OF n TERMS IN G.P.\n\n";
        cout<<"Enter value of a - ";
        int a;
        cin>>a;
        cout<<"Enter value of r - ";
        int r;
        cin>>r;
        cout<<"Enter value of n - ";
        int n;
        cin>>n;
        int p=pow(r,n);
        int q=1-p;
        int t=1-r;
        int sn=(a*q)/t;
        cout<<"Sum of "<<n<<" terms of the G.P. is "<<sn;
    }
    
    else if(c=='F')
    {
        cout<<"                         \n\nGEOMETRIC MEAN IN G.P.\n\n";
        cout<<"Enter two numbers a and b to find their geometric mean\n";
        int a,b;
        cin>>a>>b;
        float gm=sqrt(a*b);
        cout<<"Geometric mean of "<<a<<" and "<<b<<" is "<<gm<<endl;
        cout<<"Thus "<<a<<", "<<gm<<", "<<b<<" are consecutive terms of a G.P.";
    }
}


    else if(ch==5)
    {
        cout<<"                         \n\nSLOPE OF A LINE\n\n";
        cout<<"Enter x and y coordinates of 1st point\n";
        cin>>p1.x>>p1.y;
        cout<<"Enter x and y coordinates of 2nd point\n";
        cin>>p2.x>>p2.y;
        int a=p2.y-p1.y;
        int b=p2.x-p1.x;
        cout<<"Slope of the line = "<<a<<" / "<<b;
    }


    else if(ch==6)
    {
        cout<<"                         \n\nCOLLINEARITY OF THREE POINTS\n\n";
        cout<<"Enter x and y coordinates of 1st point\n";
        cin>>p1.x>>p1.y;
        cout<<"Emter x and y coordinates of 2nd point\n";
        cin>>p2.x>>p2.y;
        cout<<"Enter x and y coordinates of 3rd point\n";
        cin>>p3.x>>p3.y;
        float a=p2.y-p1.y;
        float b=p2.x-p1.x;
        float m1=a/b;
        float c=p3.y-p2.y;
        float d=p3.x-p2.x;
        float m2=c/d;

        if(m1==m2)
            cout<<"The points are collinear ";
        else
            cout<<"The points are not collinear";
    }


    else if(ch==7)
    {
        cout<<"                         \n\n3 - D GEOMETRY\n\n";
        cout<<"Enter A to find distance between 2 points\n";
        cout<<"Enter B to find coordinates of the point which divides the line segment internally\n";
        cout<<"Enter C to find coordinates of the point which divides the line segment externally\n";
        cout<<"Enter D to find coordinates of the mid-point of the line segment \n";
        cout<<"Enter E to find coordinates of the centroid of a triangle\n";
        char c;
        cin>>c;
        clrscr();
        
        if(c=='A')
        {
            cout<<"                         \n\nDISTANCE BETWEEN TWO POINTS\n\n";
            cout<<"Enter x, y and z coordinates of 1st point\n";
            cin>>p1.x>>p1.y>>p1.z;
            cout<<"Enter x, y and z coordinates of 2nd point\n";
            cin>>p2.x>>p2.y>>p2.z;
            float a=(p2.x-p1.x)*(p2.x-p1.x);
            float b=(p2.y-p1.y)*(p2.y-p1.y);
            float c=(p2.z-p1.z)*(p2.z-p1.z);
            float d=a+b+c;
            float t=sqrt(d);
            cout<<"Distance between the point = "<<t<<"units";
        }
    
        else if(c=='B')
        {
            cout<<"                         \n\nCOORDINATES OF POINT DIVIDING A LINE SEGMENT INTERNALLY\n\n";
            cout<<"Enter x, y and z coordinates of 1st point\n";
            cin>>p1.x>>p1.y>>p1.z;
            cout<<"Enter x, y and z coordinates of 2nd point \n";
            cin>>p2.x>>p2.y>>p2.z;
            cout<<"Enter ratio \n";
            int m,n;
            cin>>m>>n;
            p3.x=((m*p2.x)+(n*p1.x))/(m+n);
            p3.y=((m*p2.y)+(n*p1.y))/(m+n);
            p3.z=((m*p2.z)+(n*p1.z))/(m+n);
            cout<<"Coordinate of the point is ("<<p3.x<<" , "<<p3.y<<" , "<<p3.z<<")";
        }
        
        else if(c=='C')
        {
            cout<<"                         \n\nCOORDINATES OF POINT DIVIDING A LINE SEGMENT EXTERNALLY\n\n";
            cout<<"Enter x, y and z coordinates of 1st point\n";
            cin>>p1.x>>p1.y>>p1.z;
            cout<<"Enter x, y and z coordinates of 2nd point\n";
            cin>>p2.x>>p2.y>>p2.z;
            cout<<"Enter ratio\n";
            int m,n;
            cin>>m>>n;
            p3.x=((m*p2.x)-(n*p1.x))/(m-n);
            p3.y=((m*p2.y)-(n*p1.y))/(m-n);
            p3.z=((m*p2.z)-(n*p1.z))/(m-n);
            cout<<"Coordinates of the point is ("<<p3.x<<" , "<<p3.y<<" , "<<p3.z<<")";
        }
        
        else if(c=='D')
        {
            cout<<"                         \n\nMID-POINT\n\n";
            cout<<"Enter x, y and z coordinates of 1st point\n";
            cin>>p1.x>>p1.y>>p1.z;
            cout<<"Enter x, y and z coordinates of 2nd point\n";
            cin>>p2.x>>p2.y>>p2.z;
            p3.x=(p1.x+p2.x)/2;
            p3.y=(p1.y+p2.y)/2;
            p3.z=(p1.z+p2.z)/2;
            cout<<"Coordinates of mid-point are ("<<p3.x<<" , "<<p3.y<<" , "<<p3.z<<")";
        }
        
        else if(c=='E')
        {
            cout<<"                         \n\nCENTROID OF A TRIANGLE\n\n";
            cout<<"Enter coordinates of 1st vertex of the triangle\n";
            cin>>p1.x>>p1.y>>p1.z;
            cout<<"Enter coordinates of 2nd vertex of the triangle\n";
            cin>>p2.x>>p2.y>>p2.z;
            cout<<"Enter coordinates of 3rd vertex of the triangle\n";
            cin>>p3.x>>p3.y>>p3.z;
            p4.x=(p1.x+p2.x+p3.x)/3;
            p4.y=(p1.y+p2.y+p3.y)/3;
            p4.z=(p1.z+p2.z+p3.z)/3;
            cout<<"Coordinates of the centroid of the triangle is ("<<p4.x<<" , "<<p4.y<<" , "<<p4.z<<")";
        }
    }
return 0;
}
