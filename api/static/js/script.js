async function fetchRandomFact() {
    const response = await fetch("/generated-fact"); 
    if (response.ok) { 
        const data = await response.json();
        document.getElementById("fact").innerText = data.fact; 
    } else {
        console.error("Error fetching fact:", response.status);
        document.getElementById("fact").innerText = "Failed to load fact."; 
    }
}
