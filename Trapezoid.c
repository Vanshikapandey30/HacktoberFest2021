#include <stdio.h>
#include <string.h>
int main()
{
    int nTrapezoid,h1[20],h2[20],i;
    float base,start,end;
    
    printf(" Enter start Point\n ");
    scanf("%f" , &start);
    printf(" Enter End Point\n ");
    scanf("%f",&end);
    printf(" Number of Trapezoid\n ");
    scanf("%d", &nTrapezoid);
    for(i=1;i<=nTrapezoid;i++)
    {
        printf(" Enter h1 of Trapezoid %d\n ",i); //height1
        scanf("%d",&h1[i]);
        printf(" Enter h2 of Trapezoid %d\n ",i); //height2
        scanf("%d",&h2[i]);
    }
    base = end - start;
    float b= base/nTrapezoid; //b is width
    float Area[nTrapezoid];
    float totalArea = 0;
    for (i=1; i<= nTrapezoid;i++)
    {
        Area[i]=0.5*(h1[i]+h2[i])*b; //formula for area of Trapezoid
    }
    for (i=1; i<= nTrapezoid;i++)
    {
        totalArea= totalArea+Area[i];
    }
    printf(" Area Under a Curve = %f sq units\n", totalArea);
    return 0;
}
