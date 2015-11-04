#ifndef MATH_H
#define MATH_H
using namespace std;
template<typename T>
class Operation
{
public:
	Operation<T>();
	Operation<T>(T x, T y);
	~Operation<T>();
	//Addition
	Operation Add(Operation &a, Operation &b);
	//Subtraction
	Operation Sub(Operation &a, Operation &b);
	//Multiplication
	Operation Multi(Operation &a, Operation &b);
	//float for Magnitude
	Operation Norm(Operation &a); //Normalizer

	float Mag(Operation &a);
	
	
	int x;
	int y;
private:
};


template<typename T>
//Constructor 
Operation<T>::Operation()
{

}
template<typename T>
Operation<T>::Operation(T X, T Y)
{
	x = X;
	y = Y;
}
template<typename T>
//Destructor
Operation<T>::~Operation()
{

}
template<typename T>
//Function to Add the Vectors/Alongside the overloaded "+" operator.
Operation<T> operator +(Operation<T> &a, Operation<T> &b)
{
	Operation o;
	//Function for Addition for both x and y
	o.x = a.x + b.x;

	o.y = a.y + b.y;

	return o;


}
template<typename T>
//Function to Sub the Vectors/Alongside the overloaded "-" operator.
Operation<T> operator -(Operation<T> &a, Operation<T> &b)
{
	Operation o;
	//Function for Subtraction for both x and y
	o.x = a.x - b.x;

	o.y = a.y - b.y;

	return o;

}
template<typename T>
//Function to obtain the Magnitude for the Vecors
float Operation<T>::Mag(Operation &a)
{
	//Template for A squared.
	T asquared;

	float Asqrt;

	asquared = (a.x * a.x) + (a.y * a.y);

	Asqrt = sqrt(asquared);

	return Asqrt;
}
template<typename T>
//Function from normalization
Operation<T> Operation<T>::Norm(Operation &a)
{
	Operation o;

	T asquared;

	float Asqrt;

	asquared = (a.x * a.x) + (a.y * a.y);

	Asqrt = sqrt(asquared);

	o.x = (a.x / Asqrt);

	o.y = (a.y / Asqrt);

	return o;
}
template<typename T>
//Function for Multiplication
Operation<T> operator *(Operation<T> &a, Operation<T> &b)
{

	Operation o;
	
	o.x = a.x * b.x;

	o.y = a.y * b.y;


	return o;

}
template<typename T>
class Vector
{
public:
	Vector<T>();
	Vector<T>(T x, T y, T z);
	~Vector<T>();

	Vector Add(Vector &a, Vector &b);
	Vector Sub(Vector &a, Vector &b);
	Vector Multi(Vector &a, Vector &b);

	float Mag(Vector &a);

	Vector Norm(Vector &a);

	int x;
	int y;
	int z;

private:


};

template<typename T>
Vector<T>::Vector()
{

}
template<typename T>
Vector<T>::Vector(T X, T Y, T Z)
{
	x = X;
	y = Y;
	z = Z;
}
template<typename T>
Vector<T>::~Vector()
{

}
template<typename T>
Vector<T> operator +(Vector<T> &a, Vector<T> &b)
{
	Vector o;
	//Function to add Vector x,y,z
	o.x = a.x + b.x;

	o.y = a.y + b.y;

	o.z = a.z + b.z;

	return o;
}
template<typename T>
Vector<T> operator -(Vector<T> &a, Vector<T> &b)
{
	Vector o;
	//Function to subtract Vector x,y,z
	o.x = a.x - b.x;

	o.y = a.y - b.x;

	o.z = a.z - b.z;

	return o;

}
template<typename T>
float Vector<T>::Mag(Vector &a)
{
	T asquared;
	//creates a float of a squared.
	float Asqrt;
	//Gives a squared a value
	asquared = (a.x * a.x) + (a.y * a.y) + (a.z * a.z);

	Asqrt = sqrt(asquared);
	//returns the float Asqrt
	return Asqrt;

}

template<typename T>
Vector<T> Vector<T>::Norm(Vector &a)
{
	Vector o;

	T asquared;

	float Asqrt;

	asquared = (a.x * a.x) + (a.y * a.y) + (a.z * a.z);

	Asqrt = sqrt(asquared);

	o.x = (a.x / Asqrt);
	o.y = (a.y / Asqrt);
	o.z = (a.z / Asqrt);

	return o;

} template<typename T>
Vector<T> operator *(Vector<T> &a, Vector<T> &b)
{
	Vector o;

	o.x = a.x * b.x;
	o.y = a.y * b.y;
	o.z = a.z * a.z;

	return o;
}

//template<typename T>
//Vector<T> operator *(Vector<T)

#endif MATH_H