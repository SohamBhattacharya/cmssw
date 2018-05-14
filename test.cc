# include <iostream>
# include <vector>


class A
{
    public:
    
    int a;
};

class B : public A
{
    public:
    
    int b;
};

class C: public B
{
    public:
    
    int c;
    
    C();
};


C::C()
{
    B::a = 1;
    B::b = 2;
    c = 3;
}

int main()
{
    C C_instance1;
    
    printf("A::a = %d, B::b = %d, C::c = %d \n", C_instance1.a, C_instance1.b, C_instance1.c);
    
    return 0;
}
