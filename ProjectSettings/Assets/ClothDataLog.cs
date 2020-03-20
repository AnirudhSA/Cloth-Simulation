using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ClothDataLog : MonoBehaviour {
    Cloth clothMesh;
    public Mesh bakedMesh;
    public Vector3[] vertices;

     void Start() {
         clothMesh = this.GetComponent<Cloth>();
        //clothMesh.BakeMesh(bakedMesh);
        //vertices = bakedMesh.vertices;
        //Debug.Log(vertices[2]);
    }

    void Update() {
        Debug.Log("Time:"+Time.time);
        vertices = clothMesh.vertices;
        //vertices = bakedMesh.vertices;
        Debug.Log(vertices[1]);
        // foreach (Vector3 v in vertices)
        // {   
        //     Debug.Log(v); 
        // }
       
    }
    
}
    
