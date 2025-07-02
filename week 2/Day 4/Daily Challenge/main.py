from flask import Flask, jsonify
import requests
import random
from db_config import connect_db

app = Flask(__name__)

@app.route('/save-countries', methods=['GET'])
def save_countries():
    try:
        url = "https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population"
        response = requests.get(url)
        response.encoding = 'utf-8'
        all_countries = response.json()
       
        
        random_countries = random.sample(all_countries, 10)
     
        conn = connect_db()
        print(conn)
        cursor = conn.cursor()

        for country in random_countries:
              name = country.get("name", {}).get("common", "N/A")
              capital = country.get("capital", ["N/A"])[0]
              flag = country.get("flags", {}).get("svg", "N/A")
              subregion = country.get("subregion", "N/A")
              population = country.get("population", 0)

              name = name.encode("utf-8", errors="ignore").decode("utf-8")
              flag = flag.encode("utf-8", errors="ignore").decode("utf-8")
              subregion = subregion.encode("utf-8", errors="ignore").decode("utf-8")

              cursor.execute("""
                  INSERT INTO countries (name, capital, flag, subregion, population)
                  VALUES (%s, %s, %s, %s, %s)
              """, (name, capital, flag, subregion, population))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": " 10 random countries saved to database"}), 201

    except Exception as e:
         return jsonify({"error": str(e)}), 500
    
@app.route('/countries', methods=['GET'])
def get_countries():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name, capital, flag, subregion, population FROM countries")
        rows = cursor.fetchall()

        countries = []
        for row in rows:
            countries.append({
                "name": row[0],
                "capital": row[1],
                "flag": row[2],
                "subregion": row[3],
                "population": row[4]
            })

        cursor.close()
        conn.close()

        return jsonify(countries), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
     app.run(debug=True)
