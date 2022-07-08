import os
import numpy
import pygltflib
from pygltflib.utils import ImageFormat, Image


def export(path, vertices, indices, texture_data=[]):

    if len(texture_data) != len(vertices):
        raise Exception("Mesh points do not match field container points.")

    indices = numpy.uint32(indices)
    vertices = numpy.float32(vertices)
    uv = numpy.float32(texture_data)

    indices_binary_blob = indices.tobytes()
    vertices_binary_blob = vertices.tobytes()
    uv_binary_blob = uv.tobytes()

    gltf = pygltflib.GLTF2(
        scene=0,
        scenes=[pygltflib.Scene(nodes=[0])],
        nodes=[pygltflib.Node(mesh=0)],
        meshes=[
            pygltflib.Mesh(
                primitives=[
                    pygltflib.Primitive(
                        attributes=pygltflib.Attributes(POSITION=1, TEXCOORD_0=2),
                        indices=0, material=0
                    )
                ]
            )
        ],
        textures=[
            pygltflib.Texture(
                source=0,
                sampler=0
            )
        ],
        samplers=[
            pygltflib.Sampler(
                magFilter=pygltflib.LINEAR,
                minFilter=9987,
                wrapS=33071,
                wrapT=33071
            )
        ],
        materials=[
            pygltflib.Material(
                pbrMetallicRoughness=pygltflib.PbrMetallicRoughness(
                    baseColorTexture=pygltflib.TextureInfo(index=0),
                    metallicFactor=0, roughnessFactor=1)
            )
        ],
        accessors=[
            pygltflib.Accessor(
                bufferView=0,
                componentType=pygltflib.UNSIGNED_INT,
                count=indices.size,
                type=pygltflib.SCALAR,
                max=[int(indices.max())],
                min=[int(indices.min())],
            ),
            pygltflib.Accessor(
                bufferView=1,
                componentType=pygltflib.FLOAT,
                count=len(vertices),
                type=pygltflib.VEC3,
                max=vertices.max(axis=0).tolist(),
                min=vertices.min(axis=0).tolist(),
            ),
            pygltflib.Accessor(
                bufferView=2,
                componentType=pygltflib.FLOAT,
                count=len(uv),
                type=pygltflib.VEC2,
                max=uv.max(axis=0).tolist(),
                min=uv.min(axis=0).tolist(),
            ),
        ],
        bufferViews=[
            pygltflib.BufferView(
                buffer=0,
                byteLength=len(indices_binary_blob),
                target=pygltflib.ELEMENT_ARRAY_BUFFER,
            ),
            pygltflib.BufferView(
                buffer=0,
                byteOffset=len(indices_binary_blob),
                byteLength=len(vertices_binary_blob),
                target=pygltflib.ARRAY_BUFFER,
            ),
            pygltflib.BufferView(
                buffer=0,
                byteOffset=len(indices_binary_blob + vertices_binary_blob),
                byteLength=len(uv_binary_blob),
                target=pygltflib.ARRAY_BUFFER,
            ),
        ],
        buffers=[
            pygltflib.Buffer(
                byteLength=len(indices_binary_blob) + len(vertices_binary_blob)
                           + len(uv_binary_blob)
            )
        ],
    )

    image = Image()
    image.uri = "texture.png"
    gltf.images.append(image)
    gltf.convert_images(ImageFormat.DATAURI, os.path.dirname(os.path.abspath(__file__)))

    gltf.set_binary_blob(indices_binary_blob + vertices_binary_blob + uv_binary_blob)

    if not str.endswith(path, '.glb'):
        path += '.glb'

    gltf.save(path)

    return path
