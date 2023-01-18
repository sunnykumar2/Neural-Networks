#include <bits/stdc++.h>
using namespace std;
double X1[2][10];
void solve(double *R, double alpha, double *W)
{

    int ep = 0;
    while (ep < 4)
    {
        double error = 0;
        double y;
        for (int k = 0; k < 2; k++)
        {
            y = W[0];
            for (int i = 1; i < 10; i++)
                y = y + (double)W[i] * X1[k][i - 1];
            error = error + (R[k] - y) * (R[k] - y);
            double help = (R[k] - y) * alpha;
            //cout << "r[k] " << R[k] << " (R[k]-y) " << help << endl;
            for (int i = 0; i < 10; i++)
            {

                if (i == 0)
                {

                    W[i] = W[i] + help;
                }
                else
                {
                    W[i] = W[i] + help * X1[k][i - 1];
                }
            }
            cout << "y " << y << endl;
            for (int i = 0; i < 10; i++)
                cout << W[i] << " ";
            cout << endl;
        }
        cout << "error after " << ep << "th " << error << endl;
        // for (int i = 0; i < 10; i++)
        //     cout << W[i] << " ";
        // cout << endl;
        ep++;
    }
}
int main()
{
    double R[2];
    double W[10];
    double alpha;
    cout << " Give 3*3 matrix" << endl;
    for (int k = 0; k < 2; k++)
    {
        for (int i = 0; i < 9; i++)
            cin >> X1[k][i];
    }
    cout << " Respective output: " << endl;
    for (int i = 0; i < 2; i++)
        cin >> R[i];
    cout << "Enter the initial weights " << endl;
    for (int i = 0; i < 10; i++)
        cin >> W[i];
    cout << "alpha " << endl;
    cin >> alpha;
    solve(R, alpha, W);
}