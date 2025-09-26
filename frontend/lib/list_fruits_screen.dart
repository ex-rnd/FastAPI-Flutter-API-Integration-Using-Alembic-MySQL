import 'dart:convert';
import 'package:http/http.dart'as http;
import 'package:flutter/material.dart';
import 'models/fruit.dart';
import 'package:sonic/config.dart' as config;

class ListFruitsScreen extends StatefulWidget {
  const ListFruitsScreen({super.key});

  @override
  State<ListFruitsScreen> createState() => _ListFruitsScreenState();
}


class _ListFruitsScreenState extends State<ListFruitsScreen> {
  Future<List<Fruit>> fetchFruits() async {
    final response = await http.get(Uri.parse('${config.apiURL}/fruits'));
    if (response.statusCode == 200) {
      final List jsonData = jsonDecode(response.body);
      return jsonData.map((json) => Fruit.fromJson(json)).toList();
    }
    else {
      throw Exception('Failed to load fruits');
    }
  }




  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Fruit>>(
        future: fetchFruits(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }

          final fruits = snapshot.data!;

          return ListView.builder(
              itemCount: fruits.length,
              itemBuilder: (context, index) {
                final fruit = fruits[index];
                return ListTile(
                  title: Text(fruit.name),
                  subtitle: Text(fruit.seedless ? 'Has Seeds' : 'Seedless'),
                );
              },
          );
        },
    );
  }
}

