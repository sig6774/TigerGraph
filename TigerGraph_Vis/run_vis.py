import pyTigerGraph as tg 
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/all_data", methods=["POST", "OPTIONS"])
def get_data():
    try:
        graph = tg.TigerGraphConnection(
            host="http://43.201.137.235",
            graphname="Recom",
            apiToken="token_id"
        )
        EDA = graph.runInstalledQuery("EDA?input_user=5")
        v_user = EDA[0]['user']
        v_movie = EDA[1]['movie']
        edges = EDA[2]['@@edge_List']
        nodes = [] 
        for i in range(len(v_user)):
            nodes.append({
                "id" : v_user[i]["attributes"]["user_id"],
                "group" : 0
            })

        for i in range(len(v_movie)):
            nodes.append({
                "id" : v_movie[i]["attributes"]["movie_id"],
                "name" : v_movie[i]["attributes"]["name"],
                "group" : 1
            })

        links = []
        for i in range(len(edges)):
            links.append({
                "source" : edges[i]["from_id"],
                "target" : edges[i]["to_id"],
                "group" : 2
            })
    
        data={"nodes" : nodes, "links" : links}
        response = jsonify(data)
        return response
        
    except Exception as ex:
        response = jsonify({"Message": str(ex)})
        return response
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)