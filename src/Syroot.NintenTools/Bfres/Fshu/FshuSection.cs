﻿using Syroot.IO;

namespace Syroot.NintenTools.Bfres.Fshu
{
    /// <summary>
    /// Represents an FSHU section in a BFRES file.
    /// </summary>
    public class FshuSection
    {
        // ---- CONSTRUCTORS -------------------------------------------------------------------------------------------

        /// <summary>
        /// Initializes a new instance of the <see cref="FshuSection"/> for the given <see cref="BfresFile"/>.
        /// The stream of the file has to be positioned at the beginning of the data. Since FSHU sections can
        /// originate from different index group in a BFRES files, the additional parameter specifies this group.
        /// </summary>
        /// <param name="reader">The <see cref="BinaryDataReader"/> providing the data.</param>
        /// <param name="group">The group from which the section originates from.</param>
        internal FshuSection(BinaryDataReader reader, int group)
        {
        }
    }
}