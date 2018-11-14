#include <math.h>

typedef struct Point {
	double x, y;
}Point;

extern int Add(int a, int b);
extern int gcd(int x, int y);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int *remainder);
extern double avg(double *a, int n);
extern double distance(Point *p1, Point *p2);
#endif
