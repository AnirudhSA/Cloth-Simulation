using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ClothVertices : MonoBehaviour
{   public float offset;
    public Mesh clothMesh;
    // Start is called before the first frame update
    public Vector3[] vertices;
    void Start()
    {
        vertices = clothMesh.vertices;

        for(int i=0;i<vertices.Length;i++)
        {
            vertices[i].x += offset;
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
