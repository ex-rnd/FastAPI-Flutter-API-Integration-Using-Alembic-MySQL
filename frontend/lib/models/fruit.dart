
class Fruit {
  final int id;
  final String name;
  final bool seedless;

  Fruit({required this.id, required this.name, required this.seedless});

  factory Fruit.fromJson(Map<String, dynamic> json) {
    
    final raw = json['seedless'];
    
    bool seedlessBool;
    
    if (raw is bool) {
      seedlessBool = raw;
    } else if (raw is num) {
      seedlessBool = raw == 1;
    } else if (raw is String) {
      seedlessBool = raw == '1' || raw.toLowerCase() == 'true';
    } else {
      seedlessBool = false; // default value if type is unexpected
    }
    
    
    
    return Fruit(
      id: json['id'] as int,
      name: json['name'] as String,
      seedless: seedlessBool,
    );
  }

}

