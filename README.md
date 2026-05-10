# 🌦️ Task 6 — Weather App (API Integration)
### Synent Technologies Python Development Internship  
### Developer: John Henry Garcia Jr

This project is my submission for **Task 6: Weather App (API Integration)**.  
The objective of this task is to build a simple, modular Python application that fetches **real‑time weather data** using a public API and displays it in a clean, readable format.

This project demonstrates:
- API requests using `requests`
- JSON parsing
- Error handling
- Environment variable usage
- Modular Python scripting

---

## 🚀 Features

### 🌍 Real‑Time Weather Lookup
- Enter any city name  
- Fetches:
  - Temperature  
  - Feels‑like temperature  
  - Weather condition  
  - Humidity  
  - Wind speed  

### 🛡️ Error Handling
Gracefully handles:
- Invalid city names  
- Missing API key  
- Network issues  
- API downtime  

### 🔐 Secure API Key Management
- Uses `.env` file  
- Keeps API key out of source code  

### 🧩 Clean Code Structure
- Modular functions  
- Easy to extend  
- Beginner‑friendly and readable  

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python 3.x |
| API | OpenWeatherMap |
| Libraries | `requests`, `python-dotenv` |
| Output | Terminal / CLI |

---

## 📂 Project Structure

```
synent-task6-weatherapp-johnhenrygarciajr/
      └── src/
        └── weather.py
      │── README.md
```


---

## 🔧 Setup Instructions

### 1️⃣ Install dependencies
Run this inside the project folder:

```bash
pip install -r requirements.txt
```

### 2️⃣ Create a .env file
Inside src/, create:
```
API_KEY=your_openweathermap_api_key_here
```

### 3️⃣ Run the application
```
python src/weather.py
```

You will be prompted to enter a city name.

---

## 📊 Example Output
```
=== Weather App ===
Enter a city name: Houston

Weather for Houston, US
-----------------------
Temperature: 82°F
Feels Like: 85°F
Condition: Clear sky
Humidity: 60%
Wind Speed: 4.5 mph
```

---

### 🧪 Error Handling Examples
❌ Invalid city → “city not found”

❌ Missing API key → “API key not found”

❌ Network issue → “Network error”

❌ API down → Friendly fallback message

---

### 🏁 Conclusion
This project fulfills all requirements for Task 6: Weather App, demonstrating:

- API integration

- JSON parsing

- CLI interaction

- Error handling

- Clean Python architecture
