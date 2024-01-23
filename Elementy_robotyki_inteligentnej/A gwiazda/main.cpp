#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>


using namespace std;

struct pole
{
    int wx;
    int wy;
    float fun;
    float g;
    float heurystyka;
    pole* rodzic;
};

bool czynalezy(int x, int y, vector<pole> zbior)
{
    for (int i=0; i < zbior.size(); i++)
    {
        if (x == zbior[i].wx && y == zbior[i].wy)
        {
            return true;
        }
    }
    return false;
}

int main()
{
    vector <vector <int>> dane;
    fstream plik;
    string tekst;
    plik.open("grid.txt");
    while (getline(plik, tekst))
    {
        vector <int> wiersz;
        for (int i = 0; i < tekst.length(); i++)
        {

            if (tekst[i] != 32)
            {
                if (tekst[i] == 48)
                {
                    wiersz.push_back(0);
                }
                else
                {
                    wiersz.push_back(5);
                }
            }
        }
        dane.push_back(wiersz);
    }
    plik.close();
    int cx = 0;
    int cy = 19;
    vector <vector <pole>> plansza;
    for (int j = 0; j < dane.size(); j++)
    {
        vector <pole> poziom;
        for (int k = 0; k < dane[j].size(); k++)
        {
            pole kwadrat;
            kwadrat.wx = j;
            kwadrat.wy = k;
            kwadrat.g = 0;
            kwadrat.rodzic = nullptr;
            if (dane[j][k] == 5)
            {
                kwadrat.heurystyka = -5.0;
                kwadrat.fun = -5.0;
            }
            else
            {
                kwadrat.heurystyka = sqrt(pow((j - cx), 2) + pow((k - cy), 2));
                kwadrat.fun = kwadrat.heurystyka;
            }
            poziom.push_back(kwadrat);
        }
        plansza.push_back(poziom);
    }
    int px = 19;
    int py = 0;
    vector <pole> ol;
    vector <pole> zl;
    zl.push_back(plansza[px][py]);
    pole* praprzodek = new pole(plansza[px][py]);
    if (px - 1 <= 19 && px - 1 >= 0)
    {
        if (plansza[px - 1][py].fun != -5.0)
        {
            plansza[px - 1][py].rodzic = praprzodek;
            plansza[px - 1][py].g = 1;
            plansza[px - 1][py].fun = plansza[px - 1][py].g + plansza[px - 1][py].heurystyka;
            ol.push_back(plansza[px - 1][py]);
        }
    }
    if (px + 1 <= 19 && px + 1 >= 0)
    {
        if (plansza[px + 1][py].fun != -5.0)
        {
            plansza[px + 1][py].rodzic = praprzodek;
            plansza[px + 1][py].g = 1;
            plansza[px + 1][py].fun = plansza[px + 1][py].g + plansza[px + 1][py].heurystyka;
            ol.push_back(plansza[px + 1][py]);
        }
    }
    if (py - 1 <= 19 && py - 1 >= 0)
    {
        if (plansza[px][py - 1].fun != -5.0)
        {
            plansza[px][py - 1].rodzic = praprzodek;
            plansza[px][py - 1].g = 1;
            plansza[px][py - 1].fun = plansza[px][py - 1].g + plansza[px][py - 1].heurystyka;
            ol.push_back(plansza[px][py - 1]);
        }
    }
    if (py + 1 <= 19 && py + 1 >= 0)
    {
        if (plansza[px][py + 1].fun != -5.0)
        {
            plansza[px][py + 1].rodzic = praprzodek;
            plansza[px][py + 1].g = 1;
            plansza[px][py + 1].fun = plansza[px][py + 1].g + plansza[px][py + 1].heurystyka;
            ol.push_back(plansza[px][py + 1]);
        }
    }
    bool czy = false;
    vector <pole> sciezka;
    while (!ol.empty())
    {
        int najmf = ol[0].fun;
        int najmi = 0;
        for (int l = 0; l < ol.size(); l++)
        {
            if (ol[l].fun < najmf)
            {
                najmf = ol[l].fun;
                najmi = l;
            }
        }
        pole najmp = ol[najmi];
        zl.push_back(najmp);
        ol.erase(ol.begin() + najmi);
        if (najmp.wx == cx && najmp.wy == cy)
        {
            cout << "Istnieje sciezka z punktu poczatkowego do celu" << endl;
            czy = true;
            cout << "Sciezka od konca do poczatku:" << endl;
            pole krok = najmp;
            cout << krok.wx << " " << krok.wy << endl;
            while (krok.rodzic != nullptr)
            {
                sciezka.push_back(krok);
                krok = *krok.rodzic;
                cout << krok.wx << " " << krok.wy << endl;
            }
            break;
        }
        int tx = najmp.wx;
        int ty = najmp.wy;
        pole* przodek = new pole(najmp);
        if (!(czynalezy(tx - 1, ty, zl)))
        {
            if (tx - 1 <= 19 && tx - 1 >= 0)
            {
                if (plansza[tx - 1][ty].fun != -5.0)
                {
                    if (plansza[tx - 1][ty].rodzic != nullptr)
                    {
                        if (plansza[tx - 1][ty].fun > najmp.g + 1 + plansza[tx - 1][ty].heurystyka)
                        {
                            plansza[tx - 1][ty].rodzic = przodek;
                            plansza[tx - 1][ty].g = najmp.g + 1;
                            plansza[tx - 1][ty].fun = plansza[tx - 1][ty].g + plansza[tx - 1][ty].heurystyka;
                            ol.push_back(plansza[tx - 1][ty]);
                        }
                    }
                    else
                    {
                        plansza[tx - 1][ty].rodzic = przodek;
                        plansza[tx - 1][ty].g = najmp.g + 1;
                        plansza[tx - 1][ty].fun = plansza[tx - 1][ty].g + plansza[tx - 1][ty].heurystyka;
                        ol.push_back(plansza[tx - 1][ty]);
                    }
                }
            }
        }
        if (!(czynalezy(tx + 1, ty, zl)))
        {
            if (tx + 1 <= 19 && tx + 1 >= 0)
            {
                if (plansza[tx + 1][ty].fun != -5.0)
                {
                    if (plansza[tx + 1][ty].rodzic != nullptr)
                    {
                        if (plansza[tx + 1][ty].fun > najmp.g + 1 + plansza[tx + 1][ty].heurystyka)
                        {
                            plansza[tx + 1][ty].rodzic = przodek;
                            plansza[tx + 1][ty].g = najmp.g + 1;
                            plansza[tx + 1][ty].fun = plansza[tx + 1][ty].g + plansza[tx + 1][ty].heurystyka;
                            ol.push_back(plansza[tx + 1][ty]);
                        }
                    }
                    else
                    {
                        plansza[tx + 1][ty].rodzic = przodek;
                        plansza[tx + 1][ty].g = najmp.g + 1;
                        plansza[tx + 1][ty].fun = plansza[tx + 1][ty].g + plansza[tx + 1][ty].heurystyka;
                        ol.push_back(plansza[tx + 1][ty]);
                    }
                }
            }
        }
        if (!(czynalezy(tx, ty - 1, zl)))
        {
            if (ty - 1 <= 19 && ty - 1 >= 0)
            {
                if (plansza[tx][ty - 1].fun != -5.0)
                {
                    if (plansza[tx][ty - 1].rodzic != nullptr)
                    {
                        if (plansza[tx][ty - 1].fun > najmp.g + 1 + plansza[tx][ty - 1].heurystyka)
                        {
                            plansza[tx][ty - 1].rodzic = przodek;
                            plansza[tx][ty - 1].g = najmp.g + 1;
                            plansza[tx][ty - 1].fun = plansza[tx][ty - 1].g + plansza[tx][ty - 1].heurystyka;
                            ol.push_back(plansza[tx][ty - 1]);
                        }
                    }
                    else
                    {
                        plansza[tx][ty - 1].rodzic = przodek;
                        plansza[tx][ty - 1].g = najmp.g + 1;
                        plansza[tx][ty - 1].fun = plansza[tx][ty - 1].g + plansza[tx][ty - 1].heurystyka;
                        ol.push_back(plansza[tx][ty - 1]);
                    }
                }
            }
        }
        if (!(czynalezy(tx, ty + 1, zl)))
        {
            if (ty + 1 <= 19 && ty + 1 >= 0)
            {
                if (plansza[tx][ty + 1].fun != -5.0)
                {
                    if (plansza[tx][ty + 1].rodzic != nullptr)
                    {
                        if (plansza[tx][ty + 1].fun > najmp.g + 1 + plansza[tx][ty + 1].heurystyka)
                        {
                            plansza[tx][ty + 1].rodzic = przodek;
                            plansza[tx][ty + 1].g = najmp.g + 1;
                            plansza[tx][ty + 1].fun = plansza[tx][ty + 1].g + plansza[tx][ty + 1].heurystyka;
                            ol.push_back(plansza[tx][ty + 1]);
                        }
                    }
                    else
                    {
                        plansza[tx][ty + 1].rodzic = przodek;
                        plansza[tx][ty + 1].g = najmp.g + 1;
                        plansza[tx][ty + 1].fun = plansza[tx][ty + 1].g + plansza[tx][ty + 1].heurystyka;
                        ol.push_back(plansza[tx][ty + 1]);
                    }
                }
            }
        }
    }
    if (!czy)
    {
        cout << "Nie istnieje sciezka od punktu poczatkowego do celu." << endl;
    }
    for (int m = 0; m < sciezka.size(); m++)
    {
        dane[sciezka[m].wx][sciezka[m].wy] = 3;
    }
    for (int n = 0; n < dane.size(); n++)
    {
        for (int o = 0; o < dane[n].size(); o++)
        {
            cout << dane[n][o] << " ";
        }
        cout << endl;
    }
    return 0;
}

