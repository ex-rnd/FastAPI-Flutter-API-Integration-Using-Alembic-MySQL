
import 'package:flutter/material.dart';
import 'create_fruits_screen.dart';
import 'list_fruits_screen.dart';



class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int _selectedIndex = 0;

  get _screens => [
    ListFruitsScreen(),
    CreateFruitsScreen(),
  ];

    void _onItemTapped(int index) {
      setState(() {
        _selectedIndex = index;
      });
    }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_selectedIndex],
      appBar: AppBar(
        title: const Text('Flutter FastAPI Testing'),
      ),
      bottomNavigationBar: BottomNavigationBar(items:
      [
        BottomNavigationBarItem(icon: Icon(Icons.list), label: "List Fruit"),
        BottomNavigationBarItem(icon: Icon(Icons.plus_one_rounded), label: "Add Fruit"),        
      ],
        currentIndex: _selectedIndex,
        onTap: _onItemTapped,
      ),

    );
  }
}

